import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_rules():
    print("Welcome to the Rock-Paper-Scissors game!")
    print("Rules:")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("Enter 1 for rock, 2 for paper, and 3 for scissors.")

def play_game():
    display_rules()

    while True:
        user_score = 0
        computer_score = 0
        choices = ['rock', 'paper', 'scissors']

        print("\nEnter your name:")
        user_name = input("Name: ")

        print("\nLet's start, " + user_name + "!")
        print("Rock, Paper, Scissors - Choose your weapon!")

        for i in range(1, 4):
            print(f"{i}: {choices[i-1]}", end=' ')
        print()

        for i in range(5):  # Play 5 innings
            user_choice = int(input("Enter your choice (1/2/3): "))
            if user_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            
            user_choice = choices[user_choice - 1]
            computer_choice = random.choice(choices)
            print(f"Computer chooses: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1

        print(f"\nFinal Score - {user_name}: {user_score}  Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play_game()
