import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from dotenv import load_dotenv
import os

# Load the dataset
df = pd.read_csv("dataset/cleaned_movies.csv")

# Optional: Fill NaN tags and process 'tags' column here
df['tags'] = df['tags'].fillna('')

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['tags'])

# Compute cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
# OMDb API setup


def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(url)
    data = response.json()

    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_url
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie_title):
    try:
        idx = df[df['title'] == movie_title].index[0]
    except IndexError:
        return [], []

    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movie_list:
        movie_title = df.iloc[i[0]].title
        recommended_titles.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))

    return recommended_titles, recommended_posters

# print("Enter the movie you want to get recommendations for:")
# movie = input()
# titles, posters = recommend(movie)
#
# print("\nTop 5 Recommended Movies:")
# for t in titles:
#     print(t)