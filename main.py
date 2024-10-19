from maze import Maze
from window import Window
from point import Point

win = Window(770, 520)

m = Maze(Point(10, 10), 10, 15, 50, 50, win)
m.solve()

win.wait_for_close()