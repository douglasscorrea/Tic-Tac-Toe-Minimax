import utils
import node
import copy
import sys
import numpy as np

id = 0

def minimax(curr_node, player):
	global id
	score_list = []
	id += 1
	score = utils.calculate_score(curr_node.get_board())
	moves = utils.get_available_moves(curr_node.get_board())

	if (score in [-1, 0, 1]):
		curr_node.set_score(score)
		return score

	for move in moves:
		new_board = utils.perform_move(copy.copy(curr_node.get_board()), move, player)
		new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, player, move)
		new_node.set_id(id)

		curr_node.add_lower(new_node)

		move_score = minimax(new_node, -1*player)

		score_list.append(move_score)
		
	if(player == 1):	# MAXIMIZING
		score = max(score_list)
		curr_node.set_score(score)
	else:	# MINIMIZING
		score = min(score_list)
		curr_node.set_score(score)

	return score