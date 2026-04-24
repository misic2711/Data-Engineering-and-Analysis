from dotenv import load_dotenv
import pandas as pd
import os
import requests


load_dotenv()
api_key = os.getenv('API_KEY')

def extract_data(file_name):
    return pd.read_csv(file_name)

def fetch_movie_data(title, year):
    response = requests.get("http://www.omdbapi.com/", params={
        "t": title,
        "y": year,
        "apikey": api_key
    })
    return response.json()

def extract_relevant_data(api_response):
    return {
        "imdb_rating": api_response.get("imdbRating"),
        "actors": api_response.get("Actors"),
        "imdb_votes": api_response.get("imdbVotes")
    }

df = extract_data('movies.csv')

for index, row in df.iterrows():
    raw_data = fetch_movie_data(row['title'], row['release_year'])
    clean_data = extract_relevant_data(raw_data)
    
    df.at[index, 'imdb_rating'] = clean_data['imdb_rating']
    df.at[index, 'actors'] = clean_data['actors']
    df.at[index, 'imdb_votes'] = clean_data['imdb_votes']

df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
df = df.sort_values(by='imdb_rating', ascending=False)

df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
df = df.sort_values(by='imdb_rating', ascending=False)

def load_data(df):
    df.to_xml('movies.xml')

load_data(df)

