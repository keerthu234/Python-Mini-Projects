import random

def get_user_choice():
    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return "rock"
        elif choice == '2':
            return "paper"
        elif choice == '3':
            return "scissors"
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win!")
    else:
        print("Result: Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n=== Round {round_number} ===")
        user = get_user_choice()
        computer = get_computer_choice()
        winner = determine_winner(user, computer)
        display_result(user, computer, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing!")
            break

        round_number += 1

if __name__ == "__main__":
    print("===== Rock-Paper-Scissors Game =====")
    play_game()
