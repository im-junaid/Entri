# Challenge 3: Stone-Paper-Scissors Game
"""
Problem:
Write a Python program to play a Stone-Paper-Scissors game against the computer.

Requirements:

The user should enter their choice: "stone", "paper", or "scissor".
The computer should randomly choose one option.
Decide the winner using these rules:
Stone beats Scissor
Scissor beats Paper
Paper beats Stone
If both choices are the same → it’s a draw
Print both choices and the result.
"""

# Code :
import random, os, time

# vars
user_score = 0
bot_score = 0
result = ""
choices = ["stone", "paper", "scissor"]


def show_banner():
    os.system('cls')
    print(f"""
 ------------------------------------------
|      Game : Stone, Papper, Scissor       |
 ------------------------------------------ 
""")

# show option 
def show_options():
    print(f"""
Options :
    1. Start New Game
    2. Continue Game
    3. Show Previous Results
    4. Show Game Description
    0. Exit Game

""")

# show current score
def show_scores():
    show_banner()
    print(f"""

Recent Scores :

Points :

    You  |  Bot     
     {user_score}       {bot_score}

""")

# show game description
def show_description():
    show_banner()
    print("""
This is a simple fun game, "Stone Paper Scissor"
you are playing with a bot.

Interact with game via options number. 

---------------- rules for points : -----------------
you: stone   , bot: scissor = You get 2 points
you: paper   , bot: stone   = You get 2 points
you: scissor , bot: paper   = You get 2 points

you: stone   , bot: stone   = draw, both get 1 points
-----------------------------------------------------

Made with ❤️ by Junaid
""")

# game logic
def game():
    show_banner()
    global user_score, bot_score, result
    bot_choice = random.choice(choices)
    print(f"""

-------------- Game Started ---------------
     Enter : stone OR paper OR scissor
""")

    while True:
        user_choice = input("Enter your choice : ").strip().lower()
        if user_choice in choices:
            break
        else:
            print(f"\n\n[ERROR] : Invalid input, try again!\n\n")

    if user_choice == bot_choice:
        user_score += 1
        bot_score += 1
        result = "both ended up in tie"

    elif (
        user_choice == "scissor"
        and bot_choice == "paper"
        or user_choice == "stone"
        and bot_choice == "scissor"
        or user_choice == "paper"
        and bot_choice == "stone"
    ):
        result = "Win"
        user_score += 2
    else:
        result = "Lose"
        bot_score += 2

    print(f"""
You selected : {user_choice} , Bot selected : {bot_choice}

Result : You {result}!

Points :

    You  |  Bot     
     {user_score}       {bot_score}
""")

show_banner()
show_options()

while True:
    try:
        choice = int(input("Select an option : ").strip())
    except:
        print("\n[ERROR] : Invalid Option selected, try again!")
        time.sleep(2)
        show_banner()
        show_options()
    else:
        if choice != 0:
            if choice == 1:
                user_score = 0
                bot_score = 0
                result = ""
                game()
            elif choice == 2:
                game()
            elif choice == 3:
                show_scores()
            elif choice == 4:
                show_description()
        else :
            break
        show_options()

print("Exiting ....!")
print("Thank you playing, see u next time")