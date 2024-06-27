import random
from art import rock,paper,scissors


continue_game = 0
your_score = 0
computer_score = 0

while continue_game == 0:
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your move:")
    print("0: Rock")
    print("1: Paper")
    print("2: Scissors")

    user_choice = int(input("Your choice: "))
    if user_choice not in [0, 1, 2]:
        print("Invalid choice! Please choose again.")
        continue

    possible_list = [0, 1, 2]
    generate_computer_response = random.choice(possible_list)

    print("Your choice:")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("Computer's choice:")
    if generate_computer_response == 0:
        print(rock)
    elif generate_computer_response == 1:
        print(paper)
    else:
        print(scissors)

    if generate_computer_response == user_choice:
        print("It's a draw!")
    elif (user_choice == 0 and generate_computer_response == 2) or \
         (user_choice == 1 and generate_computer_response == 0) or \
         (user_choice == 2 and generate_computer_response == 1):
        print("You win!")
        your_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Your Score is: {your_score}\nComputer Score is: {computer_score}")

    continue_game = int(input("Do you want to play again? Type 0 for Yes and 1 for No: "))

print("Thank you for playing!")
if your_score>computer_score:
    print("You win the game!")
elif your_score==computer_score:
    print("It's a Draw")
else:
    print("Computer wins the game!")
