#from math import inf as infinity
import numpy as np
import copy
import node


def create_board():
	board = np.zeros((3,3))

	board[0][0] = 0
	board[0][1] = 0
	board[0][2] = 0
	board[1][0] = 0
	board[1][1] = 0
	board[1][2] = 0
	board[2][0] = 0
	board[2][1] = 0
	board[2][2] = 0

	return board


def get_available_moves(board):
	moves = []
	for i in range(0,len(board)):
		for j in range(0,len(board)):
			if(board[i][j] == 0):
				moves.append([i,j])

	return moves


def perform_move(board, move, player):
	board[move[0]][move[1]] = player

	return board


def calculate_score(board, player):
	win_states = [
		[board[0][0], board[0][1], board[0][2]],
		[board[1][0], board[1][1], board[1][2]],
		[board[2][0], board[2][1], board[2][2]],
		[board[0][0], board[1][0], board[2][0]],
		[board[0][1], board[1][1], board[2][1]],
		[board[0][2], board[1][2], board[2][2]],
		[board[0][0], board[1][1], board[2][2]],
		[board[2][0], board[1][1], board[0][2]],
	]
	if [player, player, player] in win_states:
		return player
	elif (len(get_available_moves(board)) == 0):
		return 0
	else:
		return -2


def calculate_score2(board, player):
	if(board[0][0] == board[1][0] == board[2][0]):
		# print('yeah')
		if(board[0][0] != 0):
			return board[0][0]

	if(board[0][1] == board[1][1] == board[2][1]):
		# print('yeah')
		if(board[0][1] != 0):
			return board[0][1]

	if(board[0][2] == board[1][2] == board[2][2]):
		# print('yeah')
		if(board[0][2] != 0):
			return board[0][2]
		
	if(board[0][0] == board[0][1] == board[0][2]):
		# print('yeah')
		if(board[0][0] != 0):
			return board[0][0]
		
	if(board[1][0] == board[1][1] == board[1][2]):
		# print('yeah')
		if(board[1][0] != 0):
			return board[1][0]
		
	if(board[2][0] == board[2][1] == board[2][2]):
		# print('yeah')
		if(board[2][0] != 0):
			return board[2][0]
		
	if(board[0][0] == board[1][1] == board[2][2]):
		# print('yeah')
		if(board[0][0] != 0):
			return board[0][0]
		
	if(board[0][2] == board[1][1] == board[2][0]):
		# print('yeah')
		if(board[0][2] != 0):
			return board[0][2]

	if(len(get_available_moves(board)) == 0):
		return 0
		
	return -2 # If there is no winning condition, return a specific score


def show_tree(nodes):
	while(len(nodes) > 0):
		node = nodes.pop(0)
		
		print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
		print('| id:' + str(node.get_id()))
		print('| depth: ' + str(node.get_depth()))
		print('| score: ' + str(node.get_score()))
		print('| player: ' + str(node.get_last_player()))
		print('| move: ' + str(node.get_move()))
		show_board(node.get_board())
		print()

		new_nodes = node.get_lowers()
		for lower in new_nodes:
			nodes.append(lower)


def show_board(board):
	print("|")
	#print("______________")
	for row in board:
		print('|   ', end='')
		for item in row:
			print('|', end='')
			if item == 0:
				print(" ", end='')
			else:
				print("X", end='') if item == 1 else print("O", end='')
			print('|', end='')
		print()
	print("|\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾", end='')