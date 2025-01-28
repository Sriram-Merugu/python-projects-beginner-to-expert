# Jarvis - A Python Virtual Assistant

This project is a Python-based virtual assistant named **Jarvis**. It can perform various tasks such as fetching the current time and date, sending emails, searching Wikipedia, taking screenshots, controlling system power (shutdown, restart, etc.), and more.

---

## Features

- **Greetings and Wishing**: Jarvis greets the user based on the current time of day (Morning, Afternoon, Evening, or Night).
- **Fetch Time and Date**: It can fetch and announce the current time and date.
- **Wikipedia Search**: Search Wikipedia for any topic and return a summarized response.
- **Email Sending**: Send emails via Gmail.
- **Screenshot**: Take a screenshot and save it to a specified path.
- **System Control**: Perform actions such as shutdown, restart, and logout.
- **Browser Search**: Open and search a query in Google Chrome.
- **Play Songs**: Automatically play music from a specified directory.
- **Memory Management**: Save and recall remembered data.
- **CPU and Battery Status**: Fetch and announce CPU usage and battery percentage.

---

## Requirements

Before running the program, make sure you have the following:

### Libraries
Install the required libraries using pip:
```bash
pip install pyttsx3 datetime SpeechRecognition wikipedia smtplib pyautogui psutil
```

## Commands You Can Use

| **Command**              | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **time**                 | Announces the current time.                                                    |
| **date**                 | Announces the current date.                                                    |
| **wikipedia <topic>**    | Searches Wikipedia and reads a summary of the topic.                           |
| **send email**           | Sends an email to the specified recipient.                                     |
| **chrome <query>**       | Searches the specified query in Google Chrome.                                 |
| **logout**               | Logs out of the current session.                                               |
| **shutdown**             | Shuts down the computer.                                                       |
| **restart**              | Restarts the computer.                                                         |
| **play songs**           | Plays a song from the configured directory.                                    |
| **remember that <data>** | Saves user-specified data for later recall.                                     |
| **do you know anything** | Recalls the data saved using "remember that."                                   |
| **screenshot**           | Takes a screenshot and saves it to the configured path.                        |
| **cpu**                  | Announces the CPU usage and battery percentage.                                |


