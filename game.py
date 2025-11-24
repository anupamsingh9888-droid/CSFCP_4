import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly.")
                print(f"You took {attempts} attempts.\n")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")

def main():
    while True:
        play_game()
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for playing! Goodbye.")
            break
        print("-" * 40)

if _name_ == "_main_":
    main()