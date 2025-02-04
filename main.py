from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800,600)
    point1 = Point(200,100)
    point2 = Point(200,300)
    line = Line(point1, point2)

    # test line draw
    # win.draw_line(line, "white")

    c = Cell(win)
    c.has_top_wall = False
    c.draw(100, 100, 150, 150)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(200, 200, 250, 250)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(100, 300, 150, 350)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(200, 400, 250, 450)
    win.wait_for_close()

main()
