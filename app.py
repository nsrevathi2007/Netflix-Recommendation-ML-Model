"""
Main Streamlit Application
"""

import streamlit as st
import pandas as pd

from data_preprocessing import load_and_preprocess_data
from recommendation import NetflixRecommender
from visualizations import (
    plot_content_type_distribution,
    plot_top_genres,
    plot_top_countries,
    plot_ratings_distribution,
    plot_release_trend
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #141414;
        color: white;
    }

    .stApp {
        background-color: #141414;
        color: white;
    }

    h1, h2, h3 {
        color: #E50914;
    }

    .recommendation-card {
        background-color: #1f1f1f;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# DATA LOADING
# ---------------------------------------------------

@st.cache_data
def load_data():
    return load_and_preprocess_data("netflix_titles.csv")


df = load_data()

# ---------------------------------------------------
# MODEL LOADING
# ---------------------------------------------------

@st.cache_resource
def load_model(dataframe):
    return NetflixRecommender(dataframe)


recommender = load_model(df)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go To",
    ["Home", "Analytics", "Recommendations"]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if menu == "Home":

    st.title("🎬 Netflix Recommendation System")

    st.write(
        """
        Discover personalized Netflix recommendations
        using Machine Learning and NLP.
        """
    )

    st.image(
        "https://images.unsplash.com/photo-1524985069026-dd778a71c7b4",
        use_container_width=True
    )

# ---------------------------------------------------
# ANALYTICS PAGE
# ---------------------------------------------------

elif menu == "Analytics":

    st.title("📊 Netflix Data Analytics")

    st.plotly_chart(
        plot_content_type_distribution(df),
        use_container_width=True
    )

    st.plotly_chart(
        plot_top_genres(df),
        use_container_width=True
    )

    st.plotly_chart(
        plot_top_countries(df),
        use_container_width=True
    )

    st.plotly_chart(
        plot_ratings_distribution(df),
        use_container_width=True
    )

    st.plotly_chart(
        plot_release_trend(df),
        use_container_width=True
    )

# ---------------------------------------------------
# RECOMMENDATION PAGE
# ---------------------------------------------------

elif menu == "Recommendations":

    st.title("🎥 Get Recommendations")

    genre_filter = st.selectbox(
        "Filter by Genre",
        ["All"] + sorted(df["listed_in"].unique())
    )

    filtered_df = df

    if genre_filter != "All":
        filtered_df = df[
            df["listed_in"].str.contains(
                genre_filter,
                case=False,
                na=False
            )
        ]

    movie_list = filtered_df["title"].sort_values().unique()

    selected_movie = st.selectbox(
        "Search Movie or TV Show",
        movie_list
    )

    if st.button("Recommend"):

        recommendations = recommender.recommend(selected_movie)

        if not recommendations:
            st.error("Movie not found in dataset.")

        else:

            st.subheader("Recommended Titles")

            for movie in recommendations:

                st.markdown(
                    f"""
                    <div class="recommendation-card">
                        <h3>{movie['title']}</h3>
                        <p><strong>Type:</strong> {movie['type']}</p>
                        <p><strong>Genre:</strong> {movie['listed_in']}</p>
                        <p><strong>Rating:</strong> {movie['rating']}</p>
                        <p><strong>Release Year:</strong> {movie['release_year']}</p>
                        <p>{movie['description']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )