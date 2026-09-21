# Smart Number Guessing Game
## Description

The Smart Number Guessing Game is a logic game that asks the user to guess a number within a limited range. The user first chooses a difficulty level. The computer then generates a random number, compares it with the user's guess, and gives feedback and a summary of how the game was played.
## How to Play
1. Choose a difficulty level.
2. The computer generates a secret number.
3. Try to guess the number within the limited attempts based on the difficulty.
4. View the summary of the recently concluded game.
5. Choose whether to play again. If yes, the game continues; if no, the game stops.

## Difficulty Levels

| Difficulty | Number Range | Attempts |
|------------|--------------|----------|
| Easy       | 1–50         | 10       |
| Medium     | 1–100        | 7        |
| Hard       | 1–200        | 5        |
## Scoring System

The score depends on the number of attempts used and the difficulty level.

Score = (Maximum Attempts - Attempts Used + 1) × Difficulty Multiplier

| Difficulty | Multiplier |
|------------|------------|
| Easy       | 1          |
| Medium     | 2          |
| Hard       | 3          |

Using fewer attempts gives a higher score.
## Input Validation

The game checks the user's input before continuing.

- Difficulty must be 1, 2, or 3.
- Guesses must be valid numbers.
- Guesses must be within the selected difficulty's range.
- Invalid input does not use up an attempt.
## How to Run

Make sure Python 3 is installed.

From the project directory, run:

```bash
python3 game.py
```
