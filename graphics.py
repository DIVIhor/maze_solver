from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.__root_widget: Tk = Tk()
        self.__root_widget.title("MazeSolver")
        self.__canvas: Canvas = Canvas(self.__root_widget, bg="white",
                                       height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running: bool = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: "Line", fill_color: str = "black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        canvas.create_line(self.start.x, self.start.y,
                           self.end.x, self.end.y,
                           fill=fill_color, width=2)


class Cell:
    def __init__(self, win: Window | None = None):
        self.__win = win
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1: int = -1
        self.__x2: int = -1
        self.__y1: int = -1
        self.__y2: int = -1
        self.visited: bool = False

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return

        left_wall = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x1, self.__y2)
        )
        wall_color = "black" if self.has_left_wall else "white"
        self.__win.draw_line(left_wall, wall_color)

        top_wall = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1)
        )
        wall_color = "black" if self.has_top_wall else "white"
        self.__win.draw_line(top_wall, wall_color)

        right_wall = Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2)
        )
        wall_color = "black" if self.has_right_wall else "white"
        self.__win.draw_line(right_wall, wall_color)

        bottom_wall = Line(
                Point(self.__x1, self.__y2),
                Point(self.__x2, self.__y2)
        )
        wall_color = "black" if self.has_bottom_wall else "white"
        self.__win.draw_line(bottom_wall, wall_color)

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        move_color = "gray"
        if not undo:
            move_color = "red"

        cell_1_mid_x = abs(self.__x2 + self.__x1) // 2
        cell_1_mid_y = abs(self.__y2 + self.__y1) // 2
        cell_2_mid_x = abs(to_cell.__x2 + to_cell.__x1) // 2
        cell_2_mid_y = abs(to_cell.__y2 + to_cell.__y1) // 2

        if self.__win is not None:
            self.__win.draw_line(Line(
                Point(cell_1_mid_x, cell_1_mid_y),
                Point(cell_2_mid_x, cell_2_mid_y)
            ), move_color)
