# Movies ETL Pipeline

ETL pipeline that loads movie data from a CSV file,
filters by country, calculates financial balance and
generates Excel reports for each country.

## What the pipeline does

1. **Extract** - loads movies.csv
2. **Filter** - filters movies by country (USA, Russia, UK, South Korea)
3. **Transform** - adds `balance` column (box_office - budget)
4. **Sort** - sorts by balance from highest to lowest
5. **Load** - generates a separate Excel file for each country (top 10 movies)

## Technologies

- Python 3
- Pandas
- OpenPyXL

## Installation

pip install -r requirements.txt

## Usage

python main.py

## Output

Generates Excel files:
- USA.xlsx
- Russia.xlsx
- UK.xlsx
- South Korea.xlsx