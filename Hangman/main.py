import random

# ASCII art logo for Hangman
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Hangman stages to represent the state of the game
stages = [
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# List of words for the game
word_list = ["sriram", "navaneeth", "ajith", "akhil", "webpage", "simple"]

# Choose a random word from the word list
chosen_word = random.choice(word_list)

# Create a display with '_' for each letter in the chosen word
display = ["_" for _ in chosen_word]

# Initialize game variables
end_of_game = False
lives = 6

print(logo)
print("Welcome to Hangman! Enter letters to guess the word:")
print(" ".join(display))

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in display:
        print(f"You've already guessed the letter '{guess}'.")
        continue

    # Update display if the guessed letter is in the chosen word
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        # Lose a life if the guessed letter is not in the word
        print(f"The letter '{guess}' is not in the word. You lose a life.")
        lives -= 1
        print(stages[6 - lives])

    # Check if the player has run out of lives
    if lives == 0:
        end_of_game = True
        print("You lost! The word was:", chosen_word)
        break

    # Check if the player has guessed the entire word
    if "_" not in display:
        end_of_game = True
        print("You won! The word is:", "".join(display))
        break

    # Display the current progress
    print(" ".join(display))
