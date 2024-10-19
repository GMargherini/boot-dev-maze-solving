from cell import Cell
from point import Point
import time, random

class Maze:
    def __init__(self, p1, rows, cols, cell_size_x, cell_size_y, win = None, seed=None):
        self.p1 = p1
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self.seed = seed
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        start = [Point(i, j) for i in range(self.p1.x, self.cell_size_x*self.cols, self.cell_size_x) for j in range(self.p1.y, self.cell_size_y*self.rows, self.cell_size_y)]
        self.cells = [[Cell(p, Point(p.x + self.cell_size_x, p.y + self.cell_size_y), self.win) for p in start[0+i*self.rows:self.rows+i*self.rows]] for i in range(0, self.cols)]
        for rows in self.cells:
            for c in rows:
                self._draw_cell(c)
        
        
    def _draw_cell(self, cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].walls["north"] = False
        self._draw_cell(self.cells[0][0])
        self.cells[self.cols-1][self.rows-1].walls["south"] = False
        self._draw_cell(self.cells[self.cols-1][self.rows-1])

    def _break_walls_r(self, i, j):
        here = self.cells[i][j]
        print(here)
        here.visited = True
        while True:
            to_visit = []
            if i != 0 and not (self.cells[i-1][j] == None) and not self.cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if j != 0 and not (self.cells[i][j-1] == None) and not self.cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if i+1 != self.cols and not (self.cells[i+1][j] == None) and not self.cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j+1 != self.rows and not (self.cells[i][j+1] == None) and not self.cells[i][j+1].visited:
                to_visit.append((i,j+1))

            if to_visit == []:
                self._draw_cell(self.cells[i][j])
                return
            else:
                r = random.seed(self.seed)
                indexes = random.choice(to_visit)
                new_cell = self.cells[indexes[0]][indexes[1]]
                if new_cell.center.x > here.center.x:
                    here.walls["east"] = False
                    new_cell.walls["west"] = False
                elif new_cell.center.x < here.center.x:
                    new_cell.walls["east"] = False
                    here.walls["west"] = False
                elif new_cell.center.y > here.center.y:
                    here.walls["south"] = False
                    new_cell.walls["north"] = False
                elif new_cell.center.y < here.center.y:
                    new_cell.walls["south"] = False
                    here.walls["north"] = False
                self._break_walls_r(indexes[0], indexes[1])
    
    def _reset_cells_visited(self):
        for cols in self.cells:
            for c in cols:
                c.visited = False

    def solve(self):
        self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        here = self.cells[i][j]
        here.visited = True
        if (i, j) == (self.cols - 1, self.rows - 1):
            return True

        if i != 0 and not (self.cells[i-1][j] == None) and not self.cells[i-1][j].visited and not here.walls["west"]:
            here.draw_move(self.cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                here.draw_move(self.cells[i-1][j], True)

        if j != 0 and not (self.cells[i][j-1] == None) and not self.cells[i][j-1].visited and not here.walls["north"]:
            here.draw_move(self.cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                here.draw_move(self.cells[i][j-1], True)

        if i+1 != self.cols and not (self.cells[i+1][j] == None) and not self.cells[i+1][j].visited and not here.walls["east"]:
            here.draw_move(self.cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                here.draw_move(self.cells[i+1][j], True)

        if j+1 != self.rows and not (self.cells[i][j+1] == None) and not self.cells[i][j+1].visited and not here.walls["south"]:
            here.draw_move(self.cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                here.draw_move(self.cells[i][j+1], True)
        
        return False