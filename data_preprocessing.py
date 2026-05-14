import re
import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))


def clean_text(text):

    if pd.isna(text):
        return ""

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    words = [word for word in words if word not in STOPWORDS]

    return " ".join(words)


def load_and_preprocess_data(file_path):

    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)

    columns = [
        "director",
        "cast",
        "country",
        "rating",
        "listed_in",
        "description"
    ]

    for col in columns:
        df[col] = df[col].fillna("Unknown")

    text_columns = [
        "director",
        "cast",
        "listed_in",
        "description"
    ]

    for col in text_columns:
        df[col] = df[col].apply(clean_text)

    df["combined_features"] = (
        df["listed_in"] + " " +
        df["cast"] + " " +
        df["director"] + " " +
        df["description"]
    )

    return df