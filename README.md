# Rock, Paper, Scissors Game

## Overview
This is a simple command-line implementation of the classic **Rock, Paper, Scissors** game. You play against the computer, and the game randomly generates the computer's choice to determine the winner.

---

## Features
- Interactive gameplay where the user can choose Rock, Paper, or Scissors.
- Randomized computer choice for a fair game.
- Displays the corresponding ASCII art for the chosen option.
- Determines and displays the winner based on the game's rules.

---

## How to Play

1. **Run the Program**:
   Run the Python script in your terminal or Python IDE.

2. **Make Your Choice**:
   When prompted, enter:
   - `0` for Rock
   - `1` for Paper
   - `2` for Scissors

3. **Computer's Choice**:
   The computer will also make a random choice.

4. **Result**:
   The program will determine and display the winner along with the choices made.

---

## Rules

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- If both choose the same option, it’s a draw.

---

## Example Gameplay

### Input
```plaintext
Welcome to the rock paper scissors game.
What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. 
1
```

### Output
```plaintext
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Computer chose: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You lose
```

---

## Code Logic

1. **Choices**:
   - Rock, Paper, and Scissors are represented using integers `0`, `1`, and `2`.

2. **User Input**:
   - Prompts the user to input their choice.

3. **Computer Choice**:
   - Generates a random choice using the `random.randint()` function.

4. **Game Rules**:
   - Compares the user's choice with the computer's choice to determine the result:
     - User wins if their choice beats the computer's choice.
     - Computer wins if its choice beats the user's choice.
     - A tie occurs when both choices are the same.

5. **ASCII Art**:
   - Displays the ASCII representation of Rock, Paper, and Scissors for both user and computer choices.

6. **Error Handling**:
   - If the user inputs an invalid number (not 0, 1, or 2), the game ends with an error message.
