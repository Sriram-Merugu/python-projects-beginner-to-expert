# Spotify Playlist Creator

## Description
This project allows users to create a Spotify playlist based on the Billboard Hot 100 chart for a specific date. By entering a date, the script fetches the corresponding song names and creates a private playlist on Spotify.

## Requirements
- Python 3.x
- `spotipy`
- `requests`
- `beautifulsoup4`

## Setup Instructions
1. Install the required libraries:
   ```bash
   pip install spotipy requests beautifulsoup4
   ```
2. Create a Spotify Developer account and set up a new application to obtain your `CLIENT_ID` and `CLIENT_SECRET`.
3. Update the `CLIENT_ID` and `CLIENT_SECRET` variables in `main.py` with your credentials.
4. Set the redirect URI in your Spotify Developer application settings to `http://example.com`.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the desired date in the format `YYYY-MM-DD` when prompted.
3. The script will create a private Spotify playlist with the top songs from the specified date.
