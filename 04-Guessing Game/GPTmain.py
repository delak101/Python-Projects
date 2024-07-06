
import random

def get_valid_input(prompt, valid_responses):
    while True:
        response = input(prompt).lower()
        if response in valid_responses:
            return response
        print(f"Please enter one of the following: {', '.join(valid_responses)}")

def play_game():
    print("Welcome to the Number Guessing Game!")
    score = 0
    name = input("Please enter your name: ")
    
    while True:
        play = get_valid_input(f"Hi {name}, want to play a guessing game? (yes/no): ", ["yes", "no"])
        if play == 'yes':
            number_to_guess = random.randint(1, 10)
            attempts = 0
            while True:
                guess = input("Guess a number between 1 and 10: ")
                if guess.isdigit():
                    guess = int(guess)
                    if 1 <= guess <= 10:
                        attempts += 1
                        if guess < number_to_guess:
                            print("Too low, try again.")
                        elif guess > number_to_guess:
                            print("Too high, try again.")
                        else:
                            print(f"Congratulations! You guessed the number in {attempts} attempts.")
                            score += 1
                            break
                    else:
                        print("Please choose a number between 1 and 10.")
                else:
                    print("Not a number. Please try again.")
            print(f"Your current score is: {score}")
        else:
            print("Thanks for playing!")
            break

play_game()
