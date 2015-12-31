#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class IllegalMoveError(Exception):
    pass

class Board(object):
    def __init__(self):
        self.cells = [None] * 9
        self.lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
            (0, 4, 8), (2, 4, 6),            # diagonal
        ]

    def is_full(self):
        return all(c is not None for c in self.cells)

    def has_won(self, player):
        for indices in self.lines:
            if all(self.cells[i] == player for i in indices):
                return True
        return False

    def update(self, player, move):
        if not 1 <= move <= 9:
            raise IllegalMoveError('Illegal move {0}, not in [1,..,9]'.format(move))
        index = move - 1 # index starts at 0
        if self.cells[index] is not None:
            raise IllegalMoveError('Illegal move {0}, "{1}" owns it!'.format(move, self.cells[index]))
        self.cells[index] = player

    def show(self, moves=False):
        # Indices are reversed for better playability with the numpad
        for i, j in ((6, 9), (3, 6), (0, 3)):
            if moves:
                print(' | '.join(str(i + 1 + j) for j in range(3)))
            else:
                print(' | '.join('.' if c is None else c for c in self.cells[i:j]))


if __name__ == '__main__':
    b = Board()
    b.show(moves=True)
    player = 'X'

    while True: # game loop
        while True: # user input loop until legal move
            move = raw_input('> Player "{0}", enter your move: '.format(player))
            try:
                b.update(player, int(move))
            except (ValueError, IllegalMoveError) as e:
                print(e)
            else:
                b.show()
                break

        if b.has_won(player):
            print('\n"{0}" has won!'.format(player))
            break

        if b.is_full():
            print('\nGame is finished, no winner...')
            break

        player = 'O' if player == 'X' else 'X' # X/O swap
