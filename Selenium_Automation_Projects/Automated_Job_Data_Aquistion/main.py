import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import json
import pymongo

# Configuration
URL = "https://pratibha.eenadu.net/notifications/latestnotifications/private-jobs/2-8-29"
JSON_FILE_PATH = "jobs.json"
MONGO_URI = "mongodb+srv://sriram:pxJlajiMicy7yVFa@cluster0.6vicwq1.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "data"
COLLECTION_NAME = "jobs"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8",
}

# Initialize translator
translator = Translator()


def translate_text(text, source_language="te", target_language="en"):
    """Translate text from source language to target language."""
    try:
        translation = translator.translate(text, src=source_language, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text


def extract_job_data(soup):
    """Extract job data from the main URL."""
    job_data = []
    for row in soup.find('tbody').find_all('tr'):
        try:
            job = {
                "img": "#",
                "organisation": translate_text(row.find_all('td')[0].text.strip()),
                "post": translate_text(row.find_all('td')[1].text.strip()),
                "lastDate": row.find_all('td')[3].text.strip(),
                "link": fetch_download_link(row.find_all('td')[4].find('a')['href']),
                "role": "public",
                "vacancies": ""
            }
            job_data.append(job)
        except Exception as e:
            print(f"Error processing row: {e}")
    return job_data


def fetch_download_link(link_url):
    """Fetch download link from the job detail page."""
    try:
        res = requests.get(link_url, headers=HEADERS)
        detail_soup = BeautifulSoup(res.text, 'html.parser')
        download_section = detail_soup.find("div", class_="download-notice")
        download_link = download_section.li.find_all('a')[-1]['href']
        return download_link
    except Exception as e:
        print(f"Error fetching download link: {e}")
        return "#"


def load_existing_data(file_path):
    """Load existing data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found. Creating a new one.")
        return []
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return []


def save_data_to_json(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been written to {file_path}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")


def upload_to_mongo(data):
    """Upload JSON data to MongoDB."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        if data:
            collection.insert_many(data)
            print("JSON data uploaded to MongoDB successfully.")
        else:
            print("No data to upload to MongoDB.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error uploading to MongoDB: {e}")
    finally:
        client.close()


def main():
    # Step 1: Fetch data from the main URL
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Extract job data
    extracted_data = extract_job_data(soup)

    # Step 3: Load existing data and merge
    existing_data = load_existing_data(JSON_FILE_PATH)
    new_data = [job for job in extracted_data if job not in existing_data]
    all_data = existing_data + new_data

    # Step 4: Save data to JSON file
    save_data_to_json(JSON_FILE_PATH, all_data)

    # Step 5: Upload to MongoDB
    upload_to_mongo(new_data)


if __name__ == "__main__":
    main()
