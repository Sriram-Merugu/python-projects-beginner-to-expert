# Hangman Game

Welcome to the **Hangman Game**! This is a Python-based implementation of the classic word-guessing game. The goal is to guess the word one letter at a time before you run out of lives. Each incorrect guess decreases your remaining lives, and the game visually shows your progress through hangman stages.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository or download the code file.
2. Navigate to the directory containing the `hangman.py` file.

---

## How to Play

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the on-screen instructions:
   - A random word will be chosen.
   - Guess one letter at a time.
   - You have 6 lives. Each incorrect guess decreases your lives and progresses the hangman drawing.

3. Win the game by guessing the entire word correctly before you run out of lives.

---

## Code Breakdown

### Key Components:

- **Word Selection:**
  A word is randomly selected from the predefined `word_list`.

- **Display:**
  The guessed word is displayed with underscores (`_`) for unguessed letters.

- **Game Logic:**
  - Tracks guessed letters to prevent duplicate inputs.
  - Handles correct and incorrect guesses.
  - Ends the game when the player either guesses the word or loses all lives.

- **ASCII Art:**
  Shows the hangman stages as the player loses lives.

---

## Example Output

### Initial State:

```
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

Welcome to Hangman! Enter letters to guess the word:
_ _ _ _ _ _
```

### During Gameplay:

```
Guess a letter: a
_ _ _ _ a _

Guess a letter: e
The letter 'e' is not in the word. You lose a life.
  +---+
  |   |
  O   |
      |
      |
      |
=========
_ _ _ _ a _
```

### Losing the Game:

```
Guess a letter: z
The letter 'z' is not in the word. You lose a life.
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
You lost! The word was: simple
```

### Winning the Game:

```
Guess a letter: s
s _ m p l e

Guess a letter: i
s i m p l e

You won! The word is: simple
```
