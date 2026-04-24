# OMDb API Movie Data Enrichment

Python script that enriches a movie dataset with IMDb ratings, 
actors and vote counts using the OMDb API.

## What the script does

1. **Extract** - loads movies.csv
2. **Fetch** - calls OMDb API for each movie
3. **Transform** - extracts IMDb rating, actors and votes
4. **Sort** - sorts movies by IMDb rating (highest first)
5. **Display** - shows top 10 movies by IMDb rating
6. **Load** - exports enriched dataset to movies.xml

## Technologies

- Python 3
- Pandas
- Requests
- python-dotenv
- lxml

## Installation

pip install -r requirements.txt

## Setup

1. Register at https://www.omdbapi.com/ and get a free API key
2. Create a `.env` file in the root folder: