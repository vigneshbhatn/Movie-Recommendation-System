import streamlit as st
from recommender import recommend
import pandas as pd

st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")

movies_df = pd.read_csv("dataset/cleaned_movies.csv")
movie_list = movies_df['title'].tolist()
movie_input = st.selectbox("Enter a movie you like:",movie_list)

if movie_input:
    titles, posters = recommend(movie_input)

    if titles:
        st.markdown("### ⭐ Top 5 Recommendations:")
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.markdown(f"**{titles[i]}**")
                st.image(
                    posters[i],
                    use_container_width=True,
                    caption="" if posters[i] != 'N/A' else "Not available"
                )
    else:
        st.warning("🚫 Sorry, movie not found in our database.")
