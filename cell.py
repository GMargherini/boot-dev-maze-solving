from point import Point
from line import Line
class Cell:
    def __init__(self, p1, p2, win=None):
        self.walls = {"north": True, "east": True, "south": True, "west": True}
        self.p1 = p1
        self.p2 = p2
        self._win = win
        self.center = Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)
        self.visited = False

    def draw(self):
        self._win.draw_line(Line(self.p1, Point(self.p2.x, self.p1.y)), "black" if self.walls["north"] else "#d9d9d9")
        self._win.draw_line(Line(Point(self.p2.x, self.p1.y), self.p2), "black" if self.walls["east"] else "#d9d9d9")
        self._win.draw_line(Line(self.p2, Point(self.p1.x, self.p2.y)), "black" if self.walls["south"] else "#d9d9d9")
        self._win.draw_line(Line(Point(self.p1.x, self.p2.y), self.p1), "black" if self.walls["west"] else "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        self._win.draw_line(Line(self.center, to_cell.center), color)

    def __str__(self):
        return f'c({self.p1}, {self.p2})'