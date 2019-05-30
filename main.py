import minimax
import numpy as np
import utils
import node
import copy
import sys

def main(argv):
	board = utils.create_board()
	print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	print("| Current board")
	utils.show_board(board)

	player = -1
	root = node.Node(-1, board, 0, -1*player, 0)

	score = minimax.minimax(copy.copy(root), player)
	print("\nScore: " + str(score))

	nodes = [root]
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

	#utils.show_tree(nodes)

if __name__ == "__main__":
    main(sys.argv)