# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Streamlit, and TMDB API. Enter a movie and get top 5 similar movies with posters.

## 🚀 Features
- Autocomplete movie selector
- TMDB API integration for posters
- Streamlit UI hosted on AWS EC2
- DuckDNS custom domain

## 🧠 Tech Stack
- Python
- Streamlit
- Scikit-learn (TF-IDF + Cosine Similarity)
- Pandas, NumPy
- TMDB API
- AWS EC2 + DuckDNS

## 📷 Screenshots
![App Screenshot](screenshots/main_ui.png)

## ⚙️ Setup Instructions
```bash
git clone https://github.com/vigneshbhatn/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
streamlit run app.py

## Live Demo
https://movierecommendationsapp.streamlit.app/
