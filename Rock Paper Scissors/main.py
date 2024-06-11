import random

winning_combinations = {
    'R': 'S',  # Rock beats Scissors
    'P': 'R',  # Paper beats Rock
    'S': 'P'   # Scissors beats Paper
}

choices = ['R', 'P', 'S']
player = None

while player != '0':
    
    #input player move
    player = input("Your Move.. \n(R -> Rock, P -> Paper, S -> Scissors)\nExit -> 0\n").upper()
    print(f"Player Move: {player}")

    #pc random choice from R P S
    pc = random.choice(choices)
    print(f"PC Move: {pc}")

    if player not in choices:
        print("Invalid input, please try again.")
        continue

    if player == pc:
        print("TIE!!")
    elif pc == winning_combinations.get(player):
        print("PLAYER WINS!!")
    else:
        print("PC WINS!!")
        