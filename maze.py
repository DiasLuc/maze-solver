from cell import Cell
import time
import random
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
            ):
        if seed is not None:
            self.seed = random.seed(seed)
        self._x1 = x1 
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_wall_r(0,0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            column = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)

        for col_index in range(self._num_cols):
            for cell_index in range(self._num_rows):
                self._draw_cell(col_index, cell_index)

    

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self.cell_size_x)
        y1 = self._y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.005)

    
    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_top_wall = False
        self._draw_cell(0,0)
        last_col_index = self._num_cols-1
        last_row_index = self._num_rows-1
        last_cell = self._cells[last_col_index][last_row_index]
        last_cell.has_bottom_wall=False
        self._draw_cell(last_col_index, last_row_index)

    def _break_wall_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = [
                (-1, 0), # Left
                (0, -1),  # Up
                (1, 0),  # Right
                (0, 1),  # Down
            ]
            possible_moves = []
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if (
                    new_i >= 0
                    and new_i < self._num_cols
                    ):
                    if (
                    new_j >= 0
                    and new_j < self._num_rows
                    and self._cells[new_i][new_j].visited != True
                    ):
                        possible_moves.append((new_i, new_j))
            if possible_moves == []:
                return
            else:
                rand_move = random.randrange(len(possible_moves))
                curr_cell_i = i
                curr_cell_j = j
                rand_cell_i = possible_moves[rand_move][0]
                rand_cell_j = possible_moves[rand_move][1]
                curr_cell = self._cells[curr_cell_i][curr_cell_j]
                rand_cell = self._cells[rand_cell_i][rand_cell_j]

                if curr_cell_i > rand_cell_i:
                    curr_cell.has_left_wall = False
                    rand_cell.has_right_wall = False
                    self._draw_cell(curr_cell_i,curr_cell_j)
                    self._draw_cell(rand_cell_i, rand_cell_j)
                elif curr_cell_i < rand_cell_i:
                    curr_cell.has_right_wall = False
                    rand_cell.has_left_wall = False
                    self._draw_cell(curr_cell_i,curr_cell_j)
                    self._draw_cell(rand_cell_i, rand_cell_j)
                elif curr_cell_j > rand_cell_j:
                    curr_cell.has_top_wall = False
                    rand_cell.has_bottom_wall = False
                    self._draw_cell(curr_cell_i,curr_cell_j)
                    self._draw_cell(rand_cell_i, rand_cell_j)
                else:
                    curr_cell.has_bottom_wall = False
                    rand_cell.has_top_wall = False
                    self._draw_cell(curr_cell_i,curr_cell_j)
                    self._draw_cell(rand_cell_i, rand_cell_j)
                self._break_wall_r(rand_cell_i, rand_cell_j)
    
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False