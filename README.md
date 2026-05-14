# 🎬 Netflix Recommendation System

A professional Netflix Recommendation System built using Machine Learning, NLP, and Streamlit.

This project uses Content-Based Filtering with TF-IDF Vectorization and Cosine Similarity to recommend similar Netflix movies and TV shows based on genres, cast, director, and descriptions.

---

# Features

- Content-Based Recommendation System
- NLP Text Preprocessing
- TF-IDF Vectorization
- Cosine Similarity Recommendations
- Interactive Streamlit Web Application
- Netflix-Inspired Dark UI
- Genre Filtering
- Recommendation Cards
- Interactive Data Visualizations
- Fast Recommendation Retrieval
- Modular and Production-Ready Code Structure

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Matplotlib
- Seaborn
- NLTK

---

# 📂 Project Structure

```bash
Netflix-Recommendation-System/
│
├── app.py
├── recommendation.py
├── data_preprocessing.py
├── visualizations.py
├── requirements.txt
├── README.md
├── netflix_titles.csv
└── assets/
```

---

# Machine Learning Concepts Used

## TF-IDF Vectorization

TF-IDF converts textual information into numerical vectors by measuring the importance of words in a document relative to the dataset.

## Cosine Similarity

Cosine Similarity measures similarity between two vectors and helps identify similar movies/shows.

---

# 📈 Exploratory Data Analysis

The project includes professional visualizations for:

- Movies vs TV Shows
- Top Genres
- Top Countries
- Ratings Distribution
- Release Trends Over Years

---

# Data Preprocessing

The dataset undergoes:

- Missing value handling
- Duplicate removal
- Lowercase conversion
- Stopword removal
- Text normalization
- Feature engineering

Combined features include:

- Genre
- Cast
- Director
- Description

---

# Installation

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd Netflix-Recommendation-System
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Download Dataset

Download the Netflix Titles dataset from Kaggle:

https://www.kaggle.com/datasets/shivamb/netflix-shows

Place:

```bash
netflix_titles.csv
```

inside the project folder.

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# Recommendation Workflow

1. Load and preprocess Netflix dataset
2. Clean and normalize textual data
3. Create combined text features
4. Apply TF-IDF Vectorization
5. Compute Cosine Similarity matrix
6. Recommend top similar movies/shows

---

# Streamlit Frontend Features

- Sidebar navigation
- Interactive charts
- Genre filtering
- Movie search dropdown
- Recommendation cards
- Responsive layout
- Dark Netflix-inspired design

---

# Deployment

This project is fully compatible with Streamlit Cloud deployment.

## Deployment Steps

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Connect GitHub repository
4. Select app.py
5. Deploy application

---

# Future Improvements

- Hybrid Recommendation System
- User Authentication
- Personalized User Profiles
- Movie Posters API Integration
- Watchlist Feature
- Deep Learning Recommendations

---

# License

This project is developed for educational and portfolio purposes.

---

# Author

Developed using Python, Machine Learning, NLP, and Streamlit.
````

