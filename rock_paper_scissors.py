import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/paper/Scissors or Q to Quitt.").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock:0 or paper:1, Scissor:2
    computer_pick = options[random_number]
    print(" Computer Picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins = + 1

    elif user_input == "scissors" and computer_pick == "pappers":
        print("You won")
        user_wins = + 1
    else:
        print("You suck ")
        computer_wins += 1
print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")

print("Goodbye!")
