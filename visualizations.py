import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


def plot_content_type_distribution(df):

    fig = px.pie(
        df,
        names="type",
        title="Movies vs TV Shows",
        hole=0.4
    )

    return fig


def plot_top_genres(df):

    genres = (
        df["listed_in"]
        .str.split(",")
        .explode()
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=genres.values,
        y=genres.index,
        orientation="h",
        title="Top Genres"
    )

    return fig


def plot_top_countries(df):

    countries = (
        df["country"]
        .str.split(",")
        .explode()
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=countries.values,
        y=countries.index,
        orientation="h",
        title="Top Countries"
    )

    return fig


def plot_ratings_distribution(df):

    fig = px.histogram(
        df,
        x="rating",
        title="Ratings Distribution"
    )

    return fig


def plot_release_trend(df):

    trend = (
        df["release_year"]
        .value_counts()
        .sort_index()
    )

    fig = px.line(
        x=trend.index,
        y=trend.values,
        title="Content Release Trend"
    )

    return fig