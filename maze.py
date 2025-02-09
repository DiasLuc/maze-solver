from cell import Cell
import time
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
            ):
        self.x1 = x1 
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)

        for col_index in range(self.num_cols):
            for cell_index in range(self.num_rows):
                self._draw_cell(col_index, cell_index)

    

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.005)

    
    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_top_wall = False
        self._draw_cell(0,0)
        last_col_index = self.num_cols-1
        last_row_index = self.num_rows-1
        last_cell = self._cells[last_col_index][last_row_index]
        last_cell.has_bottom_wall=False
        self._draw_cell(last_col_index, last_row_index)