import os
import sys
import copy
import node
import utils
import minimax
import game
import random

def main(argv):
	os.system("clear")
	board = utils.create_board()
	print("Player 1 or 2?: ", end='')
	player = input()
	player = 1 if (player == "1") else -1

	if player == -1:
		moves = utils.get_available_moves(board)
		random_move = random.randint(0, len(moves))
		board = utils.perform_move(board, moves[random_move], -1*player)

	end_score, board = game.game(player, board)

	os.system('clear')
	utils.show_board(board)
	print()
	if end_score == 0:
		print("Tied game")
	elif player == 1:
		if end_score == -1:
			print("You lose")
		else:
			print("You win")
	elif player == -1:
		if end_score == -1:
			print("You win")
		else:
			print("You lose")
		
	return

if __name__ == "__main__":
    main(sys.argv)