#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function


class IllegalMoveError(Exception):
    pass


class Board(object):
    def __init__(self):
        self.cells = [None for _ in range(9)]
        self.lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
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
            raise IllegalMoveError('Illegal move {0}, outside of 1-9'.format(move))
        index = move - 1 # index starts at 0
        if self.cells[index] is not None:
            raise IllegalMoveError('Illegal move {0}, {1} owns it!'.format(move, self.cells[index]))
        self.cells[index] = player

    def show(self):
        # Indices are reversed for better playability with the numpad
        for i, j in ((6, 9), (3, 6), (0, 3)):
            print(' | '.join('.' if c is None else c for c in self.cells[i:j]))


def main():
    b = Board()
    player = 'X'

    while True: # game loop
        b.show()
        while True: # user input loop until legal move
            move = raw_input('> Player {0}, enter your move: '.format(player))
            try:
                b.update(player, int(move))
            except (ValueError, IllegalMoveError) as e:
                print(e)
            else:
                break

        if b.has_won(player):
            b.show()
            print('{0} has won!'.format(player))
            break

        if b.is_full():
            b.show()
            print('Game is finished, no winner...')
            break

        player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
    main()
