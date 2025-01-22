# Quiz Game

This is a simple **Quiz Game** implemented in Python that tests your knowledge through multiple-choice questions. The game uses object-oriented programming principles and has a modular structure for easy customization and scalability.

## Features

- Loads questions and answers from a predefined dataset.
- Tracks your score as you progress through the quiz.
- Displays your final score upon completion.

## Project Structure

The project is organized into the following components:

1. **`question_model.py`**: Contains the `Question` class to represent each question and its answer.
2. **`data.py`**: Provides the `question_data` dictionary as the source of quiz questions and answers.
3. **`quiz_brain.py`**: Implements the `QuizBrain` class, managing the quiz logic, user interaction, and score tracking.
4. **Main Script**: Initializes the game, loads questions into a `question_bank`, and handles the game flow.

## How It Works

1. **Load Questions**: The program reads questions and answers from `data.py` and creates a list of `Question` objects (`question_bank`).
2. **Start Quiz**: The `QuizBrain` class manages the quiz, asking one question at a time and validating your answers.
3. **Track Score**: At the end of the quiz, your total score is displayed.

## How to Run

1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Make sure all required files (`question_model.py`, `data.py`, `quiz_brain.py`) are in the same directory as the main script.
4. Run the main script:
   ```bash
   python main.py
    ```

## Example Output

```
Q1: Is Python an interpreted language? (True/False): True
Correct!

Q2: Is JavaScript a server-side language? (True/False): False
Wrong!

You've completed the quiz.
Your final score was: 1/2

```
