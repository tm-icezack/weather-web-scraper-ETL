# 🌦️ NOAA Weather Data Scraper ETL

A Python ETL pipeline that scrapes weather data file listings from the [NOAA National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov/) website, filters files by modification date, downloads matching CSV files, and performs basic temperature analysis.

---

## ✨ Features

- Scrapes NOAA directory listings
- Extracts file names and last modified dates
- Filters files by a target modification date
- Downloads matching CSV weather data files
- Reads CSV data with Pandas
- Cleans temperature columns
- Finds the hottest recorded temperature
- Displays records with the highest temperature
- Runs with Docker Compose

---

## 🗂️ Project Structure

```
weather-web-scraper-etl/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── data/
```

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Requests | HTTP requests |
| BeautifulSoup4 | HTML parsing |
| Pandas | Data analysis |
| Docker | Containerization |
| Docker Compose | Container orchestration |

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd weather-web-scraper-etl
```

### 2. Create `requirements.txt`

```
beautifulsoup4
lxml
pandas
requests
```

### 3. Create `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### 4. Create `docker-compose.yml`

```yaml
version: '3.9'

services:
  weather-etl:
    build: .
    container_name: weather_etl_project
    volumes:
      - .:/app
    restart: unless-stopped
```

---

## ▶️ Running the Project

### Build and Start Container

```bash
docker compose up --build
```

### Run in Background

```bash
docker compose up -d
```

### Stop Container

```bash
docker compose down
```

---
