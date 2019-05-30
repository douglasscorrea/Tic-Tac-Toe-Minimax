import minimax
import numpy as np
import utils
import node
import copy
import sys

def main(argv):
	player = 1
	board = utils.create_board()

	print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	print("| Current board")
	utils.show_board(board)
	print()

	root = node.Node(-1, board, 0, -1*player, 0, 0)

	score = minimax.minimax(copy.copy(root), player)

	if score in [-1, 1]:	
		print("X ganhou o jogo") if score == 1 else print("O ganhou o jogo")
		return

	print("Score: " + str(score))

	lowers = root.get_lowers()
	best_score = lowers[0].get_score()
	move = lowers[0].get_move()

	for lower in lowers:
		if player == 1:
			if(lower.get_score() > best_score):
				best_score = lower.get_score()
				move = lower.get_move()
		else:
			if(lower.get_score() < best_score):
				best_score = lower.get_score()
				move = lower.get_move()
	print("Best move: " + str(move))

	#utils.show_tree([root])

if __name__ == "__main__":
    main(sys.argv)