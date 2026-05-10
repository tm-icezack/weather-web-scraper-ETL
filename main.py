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

target_date = "2024-01-19 14:51"
df_filtered = df[df["date_modified"] == target_date]
print(df_filtered)


#check if the file exists in the filtered DataFrame
if df_filtered.empty:
    print(f"No file found with date modified: {target_date}")
else:
    file_name = df_filtered.iloc[0]["file_name"]
    print(f"File found: {file_name}")

#build url to download the file

file_url = url + file_name
print(f"File URL: {file_url}")


#download the file and check if link is valid
response= requests.get(file_url,stream=True,timeout=10)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"File '{file_name}' downloaded successfully.")
else:
    print(f"failed to download file:{response.status_code}")    