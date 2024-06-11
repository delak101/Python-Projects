import random

# Define winning combinations
WINNING_COMBINATIONS = {
    'R': 'S',  # Rock beats Scissors
    'P': 'R',  # Paper beats Rock
    'S': 'P'   # Scissors beats Paper
}

# Define valid choices
CHOICES = ['R', 'P', 'S']

# Define the prompt message
PROMPT = """
Your Move..
(R -> Rock, P -> Paper, S -> Scissors)
Exit -> 0
"""

def get_player_move():
    """Prompt the player for their move and return it."""
    while True:
        move = input(PROMPT).upper()
        if move in CHOICES or move == '0':
            return move
        print("Invalid input, please try again.")

def get_pc_move():
    """Return a random move for the PC."""
    return random.choice(CHOICES)

def display_scores(score_player, score_pc):
    """Display the current scores."""
    print(f"Score: PLAYER {score_player} : PC {score_pc}")

def determine_winner(player_move, pc_move):
    """Determine the winner of the round."""
    if player_move == pc_move:
        return "TIE"
    elif pc_move == WINNING_COMBINATIONS.get(player_move):
        return "PLAYER"
    else:
        return "PC"

def main():
    score_player = 0
    score_pc = 0
    player_move = None

    while player_move != '0':
        display_scores(score_player, score_pc)
        player_move = get_player_move()

        if player_move == '0':
            break

        pc_move = get_pc_move()
        print(f"Player Move: {player_move}")
        print(f"PC Move: {pc_move}")

        winner = determine_winner(player_move, pc_move)

        if winner == "TIE":
            print("TIE!!")
        elif winner == "PLAYER":
            print("PLAYER WINS!!")
            score_player += 1
        else:
            print("PC WINS!!")
            score_pc += 1

if __name__ == "__main__":
    main()
