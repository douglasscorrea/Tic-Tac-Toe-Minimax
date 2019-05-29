import minimax
import numpy as np
import utils
import node
import copy
import sys

def main(argv):
	board = np.zeros((3,3))

	board[0][0] = 1
	board[0][1] = 0
	board[0][2] = -1
	board[1][0] = 0
	board[1][1] = 0
	board[1][2] = 1
	board[2][0] = 1
	board[2][1] = 0
	board[2][2] = -1
	print(board)
	print("###")

	player = -1
	root = node.Node(-1, board, 0, -1*player, 0)

	pontos = minimax.minimax(copy.copy(root), player)
	print(pontos)

	nodes = [root]
	filhos = root.get_lowers()
	max_score = filhos[0].get_score()
	move = filhos[0].get_move()
	# print('types ' + str(move))
	for filho in filhos:
		# print('Move' + str(filho.get_move()))
		# print('Score ' + str(filho.get_score()))
		if player == 1:
			if(filho.get_score() > max_score):
				max_score = filho.get_score()
				move = filho.get_move()
		else:
			if(filho.get_score() < max_score):
				max_score = filho.get_score()
				move = filho.get_move()
	print(move)

	utils.show_tree(nodes)

if __name__ == "__main__":
    main(sys.argv)