# Selenium Automation Projects

This repository contains Python scripts that utilize Selenium WebDriver for automating various web tasks. Each script is designed to perform a specific task, from web scraping to form submission and navigation.

---

## Project Files

### 1. **amazon_navigation.py**
- **Description**: 
  This script opens Amazon's homepage and retrieves the names of navigation links.

### 2. **cookie_clicker_bot.py**
- **Description**: 
  Automates the Cookie Clicker game by clicking the cookie and purchasing upgrades. The script also prints the cookies-per-second value for analysis.

### 3. **linkedin_login_automation.py**
- **Description**: 
  Automates the login process for LinkedIn by entering the username and password.

### 4. **InstaAutoLogin.py**
- **Description**: 
  Automates the login process for Instagram while mimicking human behavior to avoid detection by Instagram's anti-bot measures.

### 5. **automated_data_scraping_google_form_submission.py**
- **Description**: 
  Automates the process of:
  - Scraping data from a website (e.g., Hacker News: titles, links, and points).
  - Filling out and submitting a Google Form with the scraped data.
  - Collecting responses in a Google Sheet for further analysis.

---

## Features

### General Features
- **Web Scraping**: Scrapes structured data such as titles, links, and metadata from websites.
- **Google Form Automation**: Automatically fills out and submits Google Forms with scraped or pre-defined data.
- **Google Sheets Integration**: Links Google Forms to Google Sheets for data storage and analysis.
- **Anti-CAPTCHA Measures**: Uses realistic headers, random delays, and human-like interaction patterns to minimize the risk of triggering CAPTCHA mechanisms.

### Example Project: Automated Data Scraping and Google Form Submission

#### Step 1: Create a Google Form
1. Go to Google Forms and create a new form.
2. Add the following fields:
   - **Title** (Short Answer)
   - **Link** (Short Answer)
   - **Points** (Short Answer)
3. Customize the form as needed (e.g., add a description or theme).
4. Copy the form URL (e.g., `https://docs.google.com/forms/d/e/sdifjii3392OdfDfsd/viewform`).

#### Step 2: Link to Google Sheets
1. Click the "Responses" tab in the Google Form.
2. Link the form to a new or existing Google Sheet to store responses automatically.

#### Step 3: Run the Script
1. Execute the automation script using Python:
   ```bash
   python automated_data_scraping_google_form_submission.py
   ```

#### Step 4: Analyze Data in Google Sheets
1. Open the linked Google Sheet.
2. View all submitted data (titles, links, and points).
3. Use the data for analysis (e.g., sort by points to find the most upvoted stories).

---

## Requirements
- Python 3.x
- Selenium WebDriver
- BeautifulSoup
- Google Chrome and ChromeDriver

### Installation
1. Install Python dependencies:
   ```bash
   pip install selenium beautifulsoup4
   ```
2. Download ChromeDriver and add it to your system's PATH.

---

## How to Use
- Clone this repository:
  ```bash
  git clone <repository-url>
  ```
- Navigate to the project directory:
  ```bash
  cd selenium-automation-projects
  ```
- Run the desired script:
  ```bash
  python <script_name>.py
  ```

---

## Disclaimer
These scripts are for educational and personal use only. Please ensure you comply with the terms of service of the websites you interact with.
