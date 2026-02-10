import random

print("ROCK PAPER SCISSORS GAME")

choices=["rock", "paper", "scissors"]

while True:
    user=input("Enter rock, paper, scissors: ").lower()
    if user not in choices:
        print("Incorrect choice")
    
    bot=random.choice(choices)
    print("Computer choice: ", bot)

    if(bot==user):
        print("It's a tie!!")
    elif(bot=="rock" and user=="paper") or (bot=="paper" and user=="scissors") or (bot=="scissors" and user=="rock"):
        print("You WIN!!")
    else:
        print("Computer WINS!!")
        
    if input("\nPlay again (y/n)?  ").lower()!='y':
        print("\n\nThanks for playing!")
        break
    else:
        print("\n")
