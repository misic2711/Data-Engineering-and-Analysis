import pandas as pd

states = ['USA', "Russia", 'UK', 'South Korea']

def extract_data(file_name):
    return pd.read_csv(file_name)

def filter_data(df, states):
    return df[df['country'].isin(states)]

def add_new_column(df):
    df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce')
    df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
    df['balance'] = df['box_office'] - df['budget']
    return df

def sort_movies(df):
    return df.sort_values(by="balance", ascending=False)

def load_data(df):
    for state in states:
        filtered = df[df['country'] == state].head(10)
        filtered.drop(columns=['country', 'language', 'duration', 'budget', 'box_office']).to_excel(f"{state}.xlsx", index=False)
    return df

def run_pipeline(file_name):
    extract_data(file_name).pipe(filter_data, states).pipe(add_new_column).pipe(sort_movies).pipe(load_data)

run_pipeline('movies.csv')




