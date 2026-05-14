import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NetflixRecommender:

    def __init__(self, dataframe):

        self.df = dataframe

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=10000,
            ngram_range=(1, 2)
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.df["combined_features"]
        )

        self.cosine_sim = cosine_similarity(self.tfidf_matrix)

        self.indices = pd.Series(
            self.df.index,
            index=self.df["title"].str.lower()
        ).drop_duplicates()

    def recommend(self, title, top_n=10):

        title = title.lower()

        if title not in self.indices:
            return []

        idx = self.indices[title]

        similarity_scores = list(
            enumerate(self.cosine_sim[idx])
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        similarity_scores = similarity_scores[1:top_n + 1]

        movie_indices = [
            i[0] for i in similarity_scores
        ]

        recommendations = self.df.iloc[movie_indices][
            [
                "title",
                "type",
                "listed_in",
                "rating",
                "release_year",
                "description"
            ]
        ]

        return recommendations.to_dict(orient="records")