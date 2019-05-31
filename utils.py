import node
import numpy as np


def create_board():
	board = np.zeros((3,3))

	return board


def get_available_moves(board):
	moves = []
	for i in range(0,len(board)):
		for j in range(0,len(board)):
			if(board[i][j] == 0):
				moves.append([i,j])

	return moves


def verify_move(board, move):
	if (int(move[0]) >= 0 and int(move[0]) <= 2) and (int(move[1]) >= 0 and int(move[1]) <= 2):
		return True if board[int(move[0])][int(move[1])] == 0 else False
	else:
		return False


def perform_move(board, move, player):
	board[int(move[0])][int(move[1])] = player

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

def verify_end_game(board, player):
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
	elif [-1*player, -1*player, -1*player] in win_states:
		return -1*player
	elif any(0 in i for i in win_states):
		return -2
	else:
		return 0


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
	i = 0
	print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	print("| Current board")
	print("|     0  1  2") 
	#print("______________")
	for row in board:
		print('|   ' + str(i), end='')
		for item in row:
			print('|', end='')
			if item == 0:
				print(" ", end='')
			else:
				print("X", end='') if item == 1 else print("O", end='')
			print('|', end='')
		print()
		i += 1
	print("|\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾", end='')