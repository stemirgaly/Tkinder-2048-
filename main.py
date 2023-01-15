from body import grid
from body import gamePanel
from body import game


if __name__ == '__main__':
    size = 4
    grid = grid.Grid(size)
    panel = gamePanel.GamePanel(grid)
    game2048 = game.Game(grid, panel)
    game2048.start()

