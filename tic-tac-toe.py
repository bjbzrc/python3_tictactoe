# IT 4401 Final project: Python tic-tac-toe
# By Brandon Buttlar, FA 2021

# This is a two player tic-tac-toe script written fully in base Python 3,
# without any additional modules needed.

# Defines win conditions
def check_win(player_pos, cur_player):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]

    for win_cons in wins:
        if all(n in player_pos[cur_player] for n in win_cons):
            # returns true if a win condition is met
            return True
    return False


# Checks for ties
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# Prints current scores
def display_scores(score_board):
    print("")
    print("\tScores:")
    players = list(score_board.keys())
    print("\t", players[0], ": ", score_board[players[0]], sep='')
    print("\t", players[1], ": ", score_board[players[1]], sep='')
    print("")


# Main gameplay loop
def single_game(cur_player):
    values = [' ' for n in range(9)]
    player_pos = {'X': [], 'O': []}

    while True:
        display_board(values)

        try:
            print("Player ", cur_player, " turn. Please pick box 1-9: ", end="")
            choice = int(input())
        except ValueError:
            print("Error, please enter 1-9")
            continue

        if choice < 1 or choice > 9:
            print("Error, value outside of range. Please enter 1-9")
            continue

        # Ensure box isn't filled
        if values[choice - 1] != ' ':
            print("Error, spot is occupied. Please enter a different spot")
            continue

        values[choice - 1] = cur_player
        player_pos[cur_player].append(choice)

        if check_win(player_pos, cur_player):
            display_board(values)
            print("Player ", cur_player, " has won the game!")
            print("\n")
            return cur_player

        if check_draw(player_pos):
            display_board(values)
            print("Cat\'s Game! The game is a tie!")
            return 'D'

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


# Formats the scoreboard display
def display_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def main():
    print("Player 1")
    player1 = input("Please enter your name: ")
    print("Player 2")
    player2 = input("Please enter your name: ")
    cur_player = player1
    player_choice = {'X': "", 'O': ""}
    options = ['X', 'O']

    score_board = {player1: 0, player2: 0}
    display_scores(score_board)

    while True:
        print(cur_player, ", please choose a token", sep='')
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        try:
            pick = int(input())
        except ValueError:
            print("Wrong input, please enter 1, 2 or 3\n")
            continue

        if pick == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif pick == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif pick == 3:
            print("Final Scores:")
            display_scores(score_board)
            break

        else:
            print("Invalid pick, please try again\n")

        winner = single_game(options[pick - 1])

        if winner != 'D':
            new_winner = player_choice[winner]
            score_board[new_winner] = score_board[new_winner] + 1

        display_scores(score_board)
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1


main()
