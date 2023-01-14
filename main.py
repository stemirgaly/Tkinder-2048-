from __future__ import print_function
try:
    import tkinter as tk # For Python 3
    import tkinter.messagebox as messagebox
except:
    import Tkinter as tk # For Python 2
    import tkMessageBox as messagebox
from body import grid
from body import gamePanel
from body import game


if __name__ == '__main__':
    size = 4
    grid = grid.Grid(size)
    panel = gamePanel.GamePanel(grid)
    game2048 = game.Game(grid, panel)
    game2048.start()

