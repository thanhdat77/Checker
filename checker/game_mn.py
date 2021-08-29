from checker.piece import Piece
import pygame
from pygame.constants import NOFRAME
from .contains import C_BLACK, C_ORANGE, C_PUR, C_TAN, SIZE_ROW_COL
from .board import Board

class Game_mn:
    def __init__(self,win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.turn = C_PUR
        self.valid_move = {}
        self.board = Board()
    
    def reset(self):
        self._init()

    def select(self,row,col):
        if self.selected:               
            result = _move(row,col)
            if not result:
                self.selected = None
                self.select(row,col) # de quy until seclect, move be true
        piece = self.board.get_piece(row ,col)
        if piece != 0  and piece.color == self.turn:
            self.selected = piece
            self.valid_move = self.board.get_valid_move(piece)
            return True
        return False


    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece ==0 and (row,col) == self.valid_move:
            self.board.move(self.select,row,col)
            self.change_turn()
        else: return False
        return True

    def change_turn(self):
        if self.turn == C_PUR :
            self.turn == C_ORANGE
        else: self.turn == C_PUR
