import random

def playCheck():
    print("please enter yes or no")
    while True:
        game = input("want to play? (yes/no)").lower()
        if game in ["yes", "no"]:
            return game
        print("please enter yes or no")
        
score = 0

name = input("Plese enter your name: ")

game = input(f"hi {name}, want to play guessing game? (yes/no)").lower()

if game == "no":
    print("Come again!")
else:
    while game == "yes":
        
        print(f"[your score is: {score}]")
        print("I'm thinking of a number between 1 and 10.")
        number_to_guess = random.randint(1, 10)
        attempts = 0

        while True:
            guess = input("guess a number between (1-10): ")

            if guess.isdigit():
                guess = int(guess)
                if 1 <= guess <= 10:
                    attempts += 1
                    if guess < number_to_guess:
                        print("Too low! Try again.")
                    elif guess > number_to_guess:
                        print("Too high! Try again.")
                    else:
                        print(f"Congratulations! You got it in {attempts} attempts.")
                        score += 1
                        break
                else:
                    print("please choose number between 1 - 10")
            else:
                print("not a number. try again")


        game = playCheck()
        
    print(f"Your final score is: {score}")
    print("Thanks for playing!")

