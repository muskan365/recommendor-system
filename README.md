🎬📚 Movie & Book Recommendation System

A Movie and Book Recommendation System built using Python, Flask, and Pandas that allows users to browse, filter, and explore both movies and books by genre and other attributes.

This project is designed as a college minor project / portfolio project, demonstrating backend development, data handling, and dynamic web rendering using Flask.

🔗 GitHub Repository:
https://github.com/muskan365/recommendor-system

🧠 Project Overview

This application provides:

🎥 Movie browsing and filtering

📚 Book browsing and genre-based recommendations

🧩 Clean separation of backend logic and frontend UI

🌐 Dynamic HTML pages rendered via Flask

📊 Dataset-driven recommendations

The system focuses on content-based filtering using genres and metadata.

✨ Features
📚 Book Module

Browse books by genre

Genre-based book filtering

Display book title, author, and cover image

Extendable to ML-based recommendations

🎬 Movie Module

Browse movies by genre

Filter movies dynamically

Display movie posters and metadata

Ready for recommendation model integration

⚙️ General Features

Flask-based backend

Bootstrap-powered UI

Jinja2 templates

Modular project structure

Easy to extend and deploy

🗂️ Project Structure
recommendor-system/
│
├── appog.py                 # Main Flask application
│
├── templates/
│   ├── index.html           # Home page
│   ├── genre.html           # Book genre selection
│   ├── movies.html          # Movies page
│   ├── filter_movies.html   # Movie filtering UI
│   └── recommend.html       # Recommendation page
│
├── static/
│   ├── css/
│   └── images/
│
├── .gitignore
└── README.md

🛠️ Technologies Used
Layer	Technology
Language	Python
Backend	Flask
Data Handling	Pandas
Templates	Jinja2
UI	Bootstrap
Version Control	Git & GitHub
⚠️ Dataset & Model Files (Important)

Due to GitHub file size limitations, large files are not included in this repository.

Ignored files include:

.csv datasets

.pkl trained models

.zip / .whl binary files

📥 To Run Locally:

Download or prepare the datasets and models

Place them in the project root directory

Ensure filenames match those referenced in appog.py

Example expected files:

Books.csv
books.pkl
books_cleaned.pkl
books_with_genre.pkl
movies.csv


ℹ️ These files are intentionally excluded to keep the repository clean and professional.

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/muskan365/recommendor-system.git
cd recommendor-system

2️⃣ Create a Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install flask pandas

4️⃣ Start the Application
python appog.py


Open in browser:

http://127.0.0.1:5000/

🧪 Application Flow

Home Page – Select books or movies

Books Section – Browse books by genre

Movies Section – Filter and explore movies

Results Page – View recommendations and details

📈 Future Enhancements

🤖 ML-based recommendation models

🔍 Search functionality

⭐ Rating & feedback system

👤 User profiles

☁️ Deployment on Render / Railway

📱 Mobile-friendly UI

🎓 Academic Use (Minor Project)

This project demonstrates:

Backend development with Flask

Data preprocessing with Pandas

Clean project structuring

Real-world GitHub practices

Suitable for:

College minor project

Portfolio showcase

Learning Flask & recommender systems

📜 License

This project is intended for educational use.
You are free to modify and extend it.

📬 Contact

For queries or contributions, open an issue on GitHub.
