import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the NOAA directory page you want to scrape
url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

# Add headers to mimic a real browser (helps avoid being blocked)
headers = {"User-Agent": "Mozilla/5.0"}

# Send HTTP GET request to fetch the page
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")


# Initialize an empty list to store extracted data
data = []

# Select all table rows (<tr>) from the page
rows = soup.select("table tr")

# Loop through each row in the table
for row in rows:
    # Find all table cells (<td>) in the current row
    cols = row.find_all("td")

    # Skip rows that don’t have enough columns (e.g., header or empty rows)
    if len(cols) < 3:
        continue

    # Extract file name from first column and remove extra whitespace
    name = cols[0].text.strip()

    # Extract last modified date from second column
    date_modified = cols[1].text.strip()

    # Skip the "Parent Directory" row (not actual data)
    if name == "Parent Directory":
        continue

    # Append extracted data as a dictionary to the list
    data.append({
        "file_name": name,
        "date_modified": date_modified
    })

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Display the first 5 rows of the DataFrame
print(df.head())