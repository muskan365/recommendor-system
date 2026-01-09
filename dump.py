import pandas as pd

# Load your dataset
df = pd.read_csv("C:/minor_project/moviesg.csv")  # replace with your file path

df = df.drop(columns=["Poster"])

df.to_csv("C:/minor_project/moviesg.csv", index=False)  # overwrites the original



