import random

# Options
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

while True:
    # User input
    user = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    
    if user == "quit":
        print("Thanks for playing!")
        break
    
    if user not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue
    
    # Computer choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    # Determine winner
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    # Display current scores
    print(f"Score -> You: {user_score}, Computer: {computer_score}\n")
