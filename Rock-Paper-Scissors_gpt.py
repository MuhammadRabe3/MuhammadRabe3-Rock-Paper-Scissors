import random

values = ['r', 's', 'p']

while True:
    user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()

    if user_choice not in values:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(values)

    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("The computer wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break