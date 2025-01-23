# Flash Card Project

## Description
The Flash Card project is a Python application designed to help users learn new languages through flashcards. The application displays French words and their English translations, allowing users to test their knowledge and track their progress.

## Features
- Randomly displays French words on flashcards.
- Flips the card to show the English translation after a few seconds.
- Users can mark words as known, which updates the list of words to learn.
- Saves progress by updating a CSV file with known words.

## Usage
1. Run the application using Python.
2. The application will load words from `data/words_to_learn.csv`. If this file is not found, it will use `data/french_words.csv` as a fallback.
3. Click the "X" button if you do not know the word, or the checkmark button if you do.
4. The application will display the next card automatically.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)
- pandas (for handling CSV files)

