# Blackjack Game

Welcome to the **Blackjack Game**! This is a simple console-based implementation of the classic card game "Blackjack," written in Python.

## Table of Contents
- [Overview](#overview)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [Installation and Usage](#installation-and-usage)
- [Code Overview](#code-overview)
- [Sample Outputs](#sample-outputs)
---

## Overview
This project is a Python-based simulation of Blackjack, also known as "21." The objective of the game is to beat the dealer by either:

1. Getting a score of 21 on the first two cards (Blackjack).
2. Reaching a final score higher than the dealer without exceeding 21.
3. Making the dealer draw cards until their hand exceeds 21.

---


## How to Play
1. The player and dealer are each dealt two cards.
2. The player is given the option to draw another card (`y`) or pass (`n`).
3. The dealer draws cards until their score is at least 17.
4. The winner is decided based on the scores.

**Rules:**
- Cards 2-10 are worth their face value.
- Face cards (J, Q, K) are worth 10 points.
- Aces (11) are worth either 11 or 1, depending on the hand value.
- If a player's score exceeds 21, they "bust" and lose.

---

## Requirements
- Python 3.7+

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Sriram-Merugu/blackjack-game.git
   cd blackjack-game
   ```
2. Run the Python script:
   ```bash
   python main.py
   ```

---

## Code Overview
The game is divided into several functions:

1. **deal_card()**: Draws a random card from the deck.
2. **calculate_score()**: Calculates the current score of the cards.
3. **compare()**: Compares the user's and dealer's scores to determine the outcome.
4. **play_game()**: Manages the game logic and flow.
5. **Main Loop**: Repeats the game as long as the user wants to play.

---

## Sample Outputs
Example of gameplay:

```
Welcome to Blackjack!

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

   Your cards: [10, 2], current score: 12
   Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [10, 2, 7], current score: 19
   Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [10, 2, 7, 5], current score: 24
   Computer's first card: 2
   Your final hand: [10, 2, 7, 5], final score: 24
   Computer's final hand: [2, 10, 5], final score: 17
You went over. You lose 😭
Do you want to play a game of Blackjack? Type 'y' or 'n': y
Welcome to Blackjack!
   Your cards: [10, 11], current score: 0
   Computer's first card: 9
   Your final hand: [10, 11], final score: 0
   Computer's final hand: [9, 3, 4, 4], final score: 20
Win with a Blackjack 😎
Do you want to play a game of Blackjack? Type 'y' or 'n': n

```
