# Job Scraper and MongoDB Uploader

This project automates the process of scraping job notifications from the Pratibha Eenadu website, translates the data from Telugu to English, stores it in a JSON file, and uploads it to a MongoDB cloud database.

## Features

*   **Web Scraping:**
    *   Scrapes job-related data (organization, post, last date, download link) from the target website.
    *   Extracts additional job details like the download link from sub-pages.
*   **Translation:**
    *   Translates job details from Telugu to English using the `googletrans` library.
*   **JSON Storage:**
    *   Saves the scraped data into a `jobs.json` file, ensuring new data is merged with existing records to avoid duplicates.
*   **MongoDB Upload:**
    *   Uploads new job data into a MongoDB cloud database for easy storage and retrieval.
*   **Error Handling:**
    *   Handles exceptions during scraping, file operations, and database uploads to ensure the script runs smoothly.

## Prerequisites

### Libraries

Ensure you have the following Python libraries installed:

*   `requests`
*   `beautifulsoup4`
*   `googletrans`
*   `pymongo`

Install them using:

```bash
pip install requests beautifulsoup4 googletrans pymongo
```

## MongoDB Setup
1. Sign up for MongoDB Atlas and create a cluster.
2. Replace the MONGO_URI variable in the script with your MongoDB connection string.

## Code Workflow
1. Scrape Data:
    - The script sends a GET request to the target website and parses the HTML using BeautifulSoup.
2. Translate Text:
    - The scraped text in Telugu is translated into English using the googletrans library.
3. Extract Additional Links:
    - For each job posting, the script navigates to a sub-page to extract the detailed download link.
4. Save to JSON:
    - The scraped data is checked against existing data in jobs.json. New records are appended to the file.
5. Upload to MongoDB:
    - New job records are uploaded to the specified MongoDB collection for storage and further analysis.

    