
import random

choices = ["paper", "scissors", "rock"]

user_input = input("What do you choose? 0: paper, 1: scissors, 2: rock\n")

if not user_input.isdigit() or int(user_input) not in range(3):
    print("Invalid choice. You lose!")
    exit()

user_choice = int(user_input)
computer_choice = random.randint(0, 2)

print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
