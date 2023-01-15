from __future__ import print_function
import tkinter.messagebox as messagebox
from body import gamePanel
import sys
from body import grid

class Game:
    '''The main game class which is the controller of the whole game.'''
    def __init__(self, grid, panel):
        self.grid = grid
        self.panel = panel
        self.start_cells_num = 2
        self.over = False
        self.won = False
        self.keep_playing = False

    def is_game_terminated(self):
        return self.over or (self.won and (not self.keep_playing))

    def start(self):
        self.add_start_cells()
        self.panel.paint()
        self.panel.root.bind('<Key>', self.key_handler)
        self.panel.root.mainloop()

    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.grid.random_cell()

    def can_move(self):
        return self.grid.has_empty_cells() or self.grid.can_merge()

    def key_handler(self, event):
        if self.is_game_terminated():
            return

        self.grid.clear_flags()
        key_value = event.keysym
        print('{} key pressed'.format(key_value))
        if key_value in gamePanel.GamePanel.UP_KEYS:
            self.up()
        elif key_value in gamePanel.GamePanel.LEFT_KEYS:
            self.left()
        elif key_value in gamePanel.GamePanel.DOWN_KEYS:
            self.down()
        elif key_value in gamePanel.GamePanel.RIGHT_KEYS:
            self.right()
        else:
            pass

        self.panel.paint()
        print('Score: {}'.format(self.grid.current_score))
        if self.grid.found_2048():
            self.you_win()
            if not self.keep_playing:
                return

        if self.grid.moved:
            self.grid.random_cell()

        self.panel.paint()
        if not self.can_move():
            self.over = True
            self.game_over()
            sys.exit("conhost.exe")
            sys.exit("python.exe")


    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')
            if messagebox.askyesno('2048', 'You Win!\n'
                                       'Are you going to continue the 2048 game?'):
                self.keep_playing = True

    def game_over(self):
        print('Game over!')
        messagebox.showinfo('2048', 'Game over\n'
                                    f'Your score is: {grid.Grid.current_score}\n')

    def up(self):
        self.grid.transpose()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.transpose()

    def left(self):
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()

    def down(self):
        self.grid.transpose()
        self.grid.reverse()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.reverse()
        self.grid.transpose()

    def right(self):
        self.grid.reverse()
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()
        self.grid.reverse()