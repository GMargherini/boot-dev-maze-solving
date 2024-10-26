from maze import Maze
from window import Window
from point import Point

rows = 25
cols = 30
cell_size_x = 25
cell_size_y = 25



win = Window(cols*cell_size_y+20, rows*cell_size_x+20)

m = Maze(rows, cols, cell_size_x, cell_size_y, win)
m.solve()

win.wait_for_close()