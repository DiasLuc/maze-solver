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
            win,
            ):
        self.x1 = x1 
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)

        for col_index in range(len(self._cells)):
            for cell_index in range(len(self._cells[col_index])):
                self._draw_cell(col_index, cell_index)

    

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell._x1 = self.x1 + (i * self.cell_size_x)
        cell._y1 = self.y1 + (j * self.cell_size_y)
        cell._x2 = cell._x1 + self.cell_size_x
        cell._y2 = cell._y1 + self.cell_size_y
        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)