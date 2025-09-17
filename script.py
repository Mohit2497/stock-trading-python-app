import requests
import os
import csv
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

LIMIT = 100

# Example ticker schema for reference
example_ticker = {
    'ticker': 'BAYAR', 
    'name': 'Bayview Acquisition Corp Right', 
    'market': 'stocks', 
    'locale': 'us', 
    'primary_exchange': 'XNAS', 
    'type': 'RIGHT', 
    'active': True, 
    'currency_name': 'usd', 
    'cik': '0001969475', 
    'composite_figi': 'BBG01KT6G6L5', 
    'share_class_figi': 'BBG01KT6G7L3', 
    'last_updated_utc': '2025-09-16T06:05:51.696761882Z'
}

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}"
tickers = []

# Get the field names from the example ticker
fieldnames = list(example_ticker.keys())

while url:
    print(f"Fetching: {url}")
    response = requests.get(url)
    data = response.json()
    
    # Check if we got results or an error
    if 'results' in data:
        # Add tickers to our list
        for ticker in data['results']:
            tickers.append(ticker)
        
        print(f"Fetched {len(data['results'])} tickers, total: {len(tickers)}")
        
        # Get next URL
        url = data.get('next_url')
        if url:
            url = f"{url}&apiKey={POLYGON_API_KEY}"
    else:
        print("API returned error or unexpected format:", data)
        break

print(f"Total tickers fetched: {len(tickers)}")

# Save to CSV file
csv_filename = 'tickers.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for ticker in tickers:
        # Ensure all fields from example_ticker are present
        row = {}
        for field in fieldnames:
            row[field] = ticker.get(field, '')  # Use empty string if field is missing
        writer.writerow(row)

print(f"Saved {len(tickers)} tickers to {csv_filename}")