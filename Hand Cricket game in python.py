import random

print("Welcome to Hand Cricket Game!")

# prompt user to select batting or bowling
choice = input("Enter 'B' for Batting or 'W' for Bowling: ").upper()

# validate user input
while choice not in ['B', 'W']:
    choice = input("Invalid choice. Enter 'B' for Batting or 'W' for Bowling: ").upper()

# initialize variables
user_score = 0
computer_score = 0
over_limit = 6

# function to simulate a turn
def play_turn():
    user_turn = int(input("Enter a number between 1 and 6: "))
    computer_turn = random.randint(1, 6)
    print("Computer's turn:", computer_turn)
    if user_turn == computer_turn:
        print("OUT!")
        return 0
    else:
        print("Scored", user_turn, "runs!")
        return user_turn

# start the game
for over in range(1, over_limit + 1):
    print("Over", over)
    if choice == 'B':
        user_score += play_turn()
        print("Your score:", user_score)
        if user_score > computer_score:
            print("You are in the lead!")
        elif user_score == computer_score:
            print("The scores are tied!")
        else:
            print("The computer is in the lead!")
    else:
        computer_score += play_turn()
        print("Computer's score:", computer_score)
        if computer_score > user_score:
            print("The computer is in the lead!")
        elif computer_score == user_score:
            print("The scores are tied!")
        else:
            print("You are in the lead!")

# declare the winner
print("Game over!")
if user_score > computer_score:
    print("You win!")
elif user_score == computer_score:
    print("The game is tied!")
else:
    print("You lose!")
