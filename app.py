import streamlit as st
import pandas as pd
from recommender import recommend

# Load movie titles
movies_df = pd.read_csv("dataset/cleaned_movies.csv")  # Update with actual path
movie_list = sorted(movies_df['title'].tolist())

st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")

# Autocomplete dropdown
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if selected_movie:
    input_poster,titles, posters = recommend(selected_movie)
    st.markdown("### 🔍 Selected Movie")
    st.image(input_poster, width=100, caption=selected_movie)
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
