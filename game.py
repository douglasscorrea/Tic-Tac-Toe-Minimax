import os
import sys
import copy
import node
import utils
import minimax

def game(player, board):
    score = -2

    while utils.verify_end_game(board, player) not in [-1, 1]:
        #os.system('clear')
        utils.show_board(board)
        print()

        print("Choose your move [x,y]: ", end='')
        move = input()

        while utils.verify_move(board, move.split(",")) == False:
            print("Invalid move. Try again: ", end='')
            move = input()

        board = utils.perform_move(board, move.split(","), player)
        root = node.Node(-1, board, 0, -1*player, 0, 0)
        score = minimax.minimax(copy.copy(root), -1*player)

        lowers = root.get_lowers()
        best_score = lowers[0].get_score()
        move = lowers[0].get_move()

        for lower in lowers:
            if player == -1:
                if(lower.get_score() > best_score):
                    best_score = lower.get_score()
                    move = lower.get_move()
            else:
                if(lower.get_score() < best_score):
                    best_score = lower.get_score()
                    move = lower.get_move()
        
        board = utils.perform_move(board, move, -1*player)

    return score, board
    #utils.show_tree([root])