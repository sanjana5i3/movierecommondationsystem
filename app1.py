import pandas as pd
import streamlit as st
import pickle
import requests
import numpy as np

# Helper functions
def fetch_movie_details(movie_id):
    """Fetch movie details from The Movie Database API."""
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    )
    return response.json()


def fetch_poster(movie_id):
    """Fetch movie poster from The Movie Database API."""
    details = fetch_movie_details(movie_id)
    return f"https://image.tmdb.org/t/p/w500/{details.get('poster_path', '')}"


def fetch_movie_trailer(movie_id):
    """Fetch movie trailer URL from The Movie Database API."""
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    )
    videos = response.json().get('results', [])
    if videos:
        return f"https://www.youtube.com/watch?v={videos[0]['key']}"
    return None


def fetch_movie_rating(movie_id):
    """Fetch movie rating from The Movie Database API."""
    details = fetch_movie_details(movie_id)
    return details.get('vote_average', 'N/A')


def fetch_movie_runtime(movie_id):
    """Fetch movie runtime from The Movie Database API."""
    details = fetch_movie_details(movie_id)
    return details.get('runtime', 'N/A')


def fetch_movie_release_date(movie_id):
    """Fetch movie release date."""
    details = fetch_movie_details(movie_id)
    return details.get('release_date', 'N/A')


def recommend(movie):
    """Recommend movies based on similarity."""
    movie_index = movies[movies['title'] == movie].index[0]
    if isinstance(similarity1, np.ndarray) and len(similarity1.shape) == 2:
        distances = similarity1[movie_index]
    else:
        st.error("Similarity matrix not loaded correctly or is empty.")
        return [], [], [], [], [], [], [], []

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_genres = []
    recommended_movies_overview = []
    recommended_movies_trailers = []
    recommended_movies_ratings = []
    recommended_movies_runtime = []
    recommended_movies_release_date = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommended_movies.append(details.get('title', 'N/A'))
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_genres.append(', '.join([genre['name'] for genre in details.get('genres', [])]))
        recommended_movies_overview.append(details.get('overview', 'No overview available'))
        recommended_movies_trailers.append(fetch_movie_trailer(movie_id))
        recommended_movies_ratings.append(fetch_movie_rating(movie_id))
        recommended_movies_runtime.append(fetch_movie_runtime(movie_id))
        recommended_movies_release_date.append(fetch_movie_release_date(movie_id))

    return recommended_movies, recommended_movies_posters, recommended_movies_genres, recommended_movies_overview, recommended_movies_trailers, recommended_movies_ratings, recommended_movies_runtime, recommended_movies_release_date


# Load data and model
try:
    movies_dict = pickle.load(open('movies_recommond_dict.pkl', 'rb'))
    similarity1 = pickle.load(open('similarity11.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
except Exception as e:
    st.error(f"Error loading data or similarity matrix: {str(e)}")

st.set_page_config(page_title="Movie Recommender System", page_icon="🎥", layout="wide")
st.title('🎬 Movie Recommender System')

# Select Box for Movie Selection
selected_movie_name = st.selectbox('Select a movie for recommendations:', movies['title'].values)

# Apply custom styles for better UI/UX
def apply_custom_styles():
    st.markdown(
        """
        <style>
        .movie-container img { transition: transform 0.2s; }
        .movie-container img:hover { transform: scale(1.05); }
        </style>
        """, unsafe_allow_html=True
    )
apply_custom_styles()


def display_movies(names, posters, ids, genres, overviews, trailers, ratings, runtimes, release_dates):
    cols = st.columns(len(names))
    for idx, col in enumerate(cols):
        with col:
            st.markdown(
                f"""<div class='movie-container'><img src='{posters[idx]}' style='width: 100%; border-radius: 10px;' /></div>""",
                unsafe_allow_html=True)
            st.caption(f"🎥 {names[idx]}")
            st.caption(f"⭐ Rating: {ratings[idx]}")
            st.caption(f"⏳ Runtime: {runtimes[idx]} min")
            st.caption(f"📅 Release Date: {release_dates[idx]}")
            if trailers[idx]:
                st.markdown(f"[🎞 Watch Trailer]({trailers[idx]})")
            with st.expander("📖 Overview"):
                st.write(overviews[idx])


if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        names, posters, genres, overviews, trailers, ratings, runtimes, release_dates = recommend(selected_movie_name)
        st.markdown("## Recommended Movies 🎬")
        display_movies(names, posters, [movies[movies['title'] == name].iloc[0]['movie_id'] for name in names], genres,
                       overviews, trailers, ratings, runtimes, release_dates)

# User Feedback Section
st.markdown("## 🤔 Did you like these recommendations?")
if st.button("👍 Yes"):
    st.success("Thanks for your feedback!")
if st.button("👎 No"):
    st.warning("We will improve our recommendations!")