#from math import inf as infinity
import numpy as np
import utils

class Node():
	def __init__(self, upper, board, depth, last_player, move):
		self.upper = upper
		self.board = board
		self.depth = depth
		self.last_player = last_player
		self.lowers = []
		self.score = -2
		self.final = 0
		self.move = move
		self.evaluated = 0
		self.id = 0
		# print('tipo ' + str(move[0]))

	def get_id(self):
		return self.id

	def set_id(self, id):
		self.id = id

	def get_upper(self):
		return self.upper

	def get_board(self):
		return self.board

	def get_last_player(self):
		return self.last_player

	def add_lower(self, lower):
		self.lowers.append(lower)

	def get_lowers(self):
		return self.lowers

	def get_depth(self):
		return self.depth

	def print_board(self):
		print(self.board)

	def set_final(self):
		self.final = 1

	def get_final(self):
		return self.final

	def set_score(self, score):
		self.score = score

	def get_score(self):
		return self.score

	def is_final(self):
		return self.final

	def get_move(self):
		return self.move

	def set_move(self, move):
		self.move = move

	def is_evaluated(self):
		return self.evaluated

	def set_evaluated(self):
		self.evaluated = 1