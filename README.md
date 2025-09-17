# Stock Ticker CSV Generator — Lesson 2

I’m following Zach Wilson’s Beginner Data Engineering Bootcamp. In this lesson I built a simple Python script that pulls stock tickers from Polygon.io and saves them to a clean CSV. It’s a small, practical step: read an API, handle multiple pages of results, and produce a file that’s ready to use.

This project contains a single script that downloads stock tickers and saves them to a CSV file.

## What `script.py` does

- Connects to Polygon.io and requests a list of stock tickers
- Follows the "next" link until all pages are fetched
- Saves the data to `tickers.csv`
- Uses the same set of columns for every row
- Stops and prints a message if the API responds with an error

## Requirements

- Python 3
- Polygon.io API key stored in a local `.env` as `POLYGON_API_KEY`
- Dependencies from `requirements.txt` installed

## How to run

1. Put your API key in `.env` (key: `POLYGON_API_KEY`)
2. Install dependencies from `requirements.txt`
3. Run the script
4. Open `tickers.csv` to see the results

## Output

- A file named `tickers.csv` with ~500 tickers and consistent columns

## Acknowledgments

This work is based on Zach Wilson’s Beginner Data Engineering Bootcamp.
- Bootcamp: [github.com/zachwilson/beginner-data-engineering-bootcamp](https://github.com/zachwilson/beginner-data-engineering-bootcamp)
- Zach’s site: [dataengineeringweekly.com](https://www.dataengineeringweekly.com/)