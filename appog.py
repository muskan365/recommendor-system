from flask import Flask,render_template,request
import pickle
import math
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import jsonify

# Load movie dataset
movies = pd.read_csv("movies_expanded.csv")

# Unique genres and directors for filtering
# Drop NaN and non-string values for genre and director lists
genres = sorted([g for g in movies["Genre"].dropna().unique() if isinstance(g, str)])
directors = sorted([d for d in movies["Director"].dropna().unique() if isinstance(d, str)])


# Combine important features into a single string
def combine_features(row):
    return f"{row['Genre']} {row['Director']} {row['Description']}"

movies["combined"] = movies.apply(combine_features, axis=1)

# Convert text to feature vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies["combined"])

# Cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Recommender function
def recommend_movie(movie_title, num_recommendations=5):
    if movie_title not in movies['Title'].values:
        return []

    idx = movies[movies['Title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    recommended_indices = [i[0] for i in similarity_scores]
    
    return movies.iloc[recommended_indices][["Title", "Genre", "Director", "Poster", "Description"]]


popular_df = pd.read_pickle('popular.pkl')
pt = pd.read_pickle('pt.pkl')
books = pd.read_pickle('books.pkl')
books = pd.read_pickle('books_with_genre.pkl')

# Check missing values
print(books.isnull().sum())
print(books[books['Book-Title'].isnull()])


# ✅ Cleanly map Genre into popular_df
books_unique = books.drop_duplicates(subset='Book-Title').set_index('Book-Title')
popular_df['Genre'] = popular_df['Book-Title'].map(books_unique['Genre'])


similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           Genre = list(popular_df['Genre'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', book_name=list(popular_df['Book-Title'].values))

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

        # ✅ Skip if temp_df is empty
        if temp_df.empty:
            print(f"Skipping: {pt.index[i[0]]} (no data found in books.pkl)")
            continue

        title = temp_df['Book-Title'].values[0]
        author = temp_df['Book-Author'].values[0]

        raw_image = temp_df['Image-URL-M'].values[0]
        image = raw_image if pd.notna(raw_image) and str(raw_image).strip() != "" else "/static/images/placeholder1.jpg"

        genre = temp_df['Genre'].values[0] if pd.notna(temp_df['Genre'].values[0]) else "Unknown"

        data.append([title, author, image, genre])

    print("Books being sent to template:", data)
    return render_template('recommend.html', data=data)


@app.route('/genre')
def genre():
    genres = books['Genre'].unique().tolist()
    return render_template("genre.html", genres=genres)

@app.route('/genre_books', methods=['POST'])
def genre_books():
    selected_genre = request.form.get('genre_input')
    filtered_books = books[books['Genre'] == selected_genre]

    return render_template('genre_books.html', genre=selected_genre, books=filtered_books)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/movies")
def show_movies():
    return render_template("movie_recommend.html", movies=movies)


@app.route("/recommend_movie/<title>")
def recommend_movie_page(title):
    recommendations = recommend_movie(title)
    return render_template("movie_recommend_result.html", movies=recommendations, base=title)

@app.route("/filter_movies", methods=["GET", "POST"])
def filter_movies():
    selected_genre = request.form.get("genre")
    selected_director = request.form.get("director")

    filtered_movies = movies.copy()

    if selected_genre and selected_genre != "All":
        filtered_movies = filtered_movies[filtered_movies["Genre"] == selected_genre]
    if selected_director and selected_director != "All":
        filtered_movies = filtered_movies[filtered_movies["Director"] == selected_director]

    return render_template("movie_filter.html",
                           movies=filtered_movies,
                           genres=["All"] + genres,
                           directors=["All"] + directors,
                           selected_genre=selected_genre,
                           selected_director=selected_director)

@app.route('/get_directors_by_genre')
def get_directors_by_genre():
    genre = request.args.get('genre')
    if genre == "All" or genre is None:
        filtered = movies
    else:
        filtered = movies[movies["Genre"] == genre]
    
    directors = sorted(filtered["Director"].dropna().unique())
    return jsonify({"directors": directors})

if __name__ == '__main__':
    app.run(debug=True)