import random

#prompt user for input
user_action = input("chose from the option (rock, scissors, paper): ")

#cpu action
cpulist = ["rock","paper", "scissors"]
computer_choice = random.choice(cpulist)

print(f"\nYou chose {user_action}, computer chose {computer_choice}.\n")

while True: 
    if user_action == computer_choice:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
