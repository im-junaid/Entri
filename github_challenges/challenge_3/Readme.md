<div align="center">

# 🎮 Stone Paper Scissors Game

A simple, interactive command-line Stone-Paper-Scissors game where you compete against a computer opponent. 
Built with Python, this game features a menu-driven interface, score tracking, and persistent gameplay across multiple rounds.

</div>

## 📸 Demo Video

![Demo GIF](https://raw.githubusercontent.com/im-junaid/Entri/refs/heads/main/github_challenges/challenge_3/game-demo.gif)

## Features

- **Interactive Menu System** - Easy-to-navigate options for starting, continuing, or reviewing games
- **Score Tracking** - Persistent score tracking across multiple rounds
- **Clear Game Rules** - Built-in game description and rules reference
- **Input Validation** - Handles invalid inputs gracefully with error messages
- **Game Statistics** - View your performance history anytime during gameplay
- **Clean Interface** - Terminal-clearing functionality for a smooth gaming experience


## How to Play
1. Download the game script file.
2. Launch the game by running the Python script
3. Select an option from the main menu:
   - **Option 1**: Start a new game (resets scores)
   - **Option 2**: Continue the current game (keeps scores)
   - **Option 3**: View previous results
   - **Option 4**: View game description and rules
   - **Option 0**: Exit the game

4. During gameplay, enter your choice: `stone`, `paper`, or `scissor`
5. The computer will randomly select its choice
6. The winner is determined and scores are updated

## Game Rules

The game follows classic Stone-Paper-Scissors rules:

- **Stone** beats **Scissor** 🪨 > ✂️
- **Scissor** beats **Paper** ✂️ > 📄
- **Paper** beats **Stone** 📄 > 🪨
- Same choices result in a **draw** 🤝

### Scoring System

- **Win**: You earn **2 points**
- **Draw**: Both players earn **1 point** each
- **Loss**: Bot earns **2 points**

## Technologies Used

- **Python 3.10+** - Core programming language
- **random** module - For generating computer choices
- **os** module - For terminal clearing
- **time** module - For display timing

**Enjoy the game!** 🎮 If you found this project helpful, please consider giving it a ⭐

*Made with ❤️ by Junaid*