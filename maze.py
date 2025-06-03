import random
from time import sleep

from graphics import Cell, Window


class Maze:
    def __init__(self, x1: int, y1: int,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Window | None = None,
                 seed: int | None = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells: list[list[Cell]] = []
        # fill the cell list and draw entry and exit points
        self.__create_cells()
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__break_entrance_and_exit()
        self.__reset_cells_visited()

    def __create_cells(self):
        self.__cells = [
            [Cell(self.__win) for _ in range(self.__num_rows)]
            for _ in range(self.__num_cols)
        ]

        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, col: int, row: int):
        if self.__win is None:
            return

        x1 = self.__x1 + col * self.__cell_size_x
        y1 = self.__y1 + row * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[col][row].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
            sleep(0.01)

    def __break_entrance_and_exit(self):
        # make an entrance
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        # make an exit
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, col: int, row: int):
        cur_cell = self.__cells[col][row]
        cur_cell.visited = True
        while True:
            to_visit = []
            if ((right := col + 1) < self.__num_cols
                and not self.__cells[right][row].visited):
                to_visit.append((right, row, "right"))
            if ((left := col - 1) >= 0
                and not self.__cells[left][row].visited):
                to_visit.append((left, row, "left"))
            if ((top := row - 1) >= 0
                and not self.__cells[col][top].visited):
                to_visit.append((col, top, "top"))
            if ((bottom := row + 1) < self.__num_rows
                and not self.__cells[col][bottom].visited):
                to_visit.append((col, bottom, "bottom"))
            
            if len(to_visit) == 0:
                self.__draw_cell(col, row)
                return
            
            next = random.choice(to_visit)
            match next[2]:
                case "right":
                    cur_cell.has_right_wall = False
                    self.__cells[next[0]][next[1]].has_left_wall = False
                case "left":
                    cur_cell.has_left_wall = False
                    self.__cells[next[0]][next[1]].has_right_wall = False
                case "top":
                    cur_cell.has_top_wall = False
                    self.__cells[next[0]][next[1]].has_bottom_wall = False
                case _:
                    cur_cell.has_bottom_wall = False
                    self.__cells[next[0]][next[1]].has_top_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next[0], next[1])

    def __reset_cells_visited(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__cells[col][row].visited = False

    def _solve_r(self, col: int, row: int):
        self.__animate()
        cur_cell = self.__cells[col][row]
        cur_cell.visited = True
        if col == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True

        down = row + 1
        if down < self.__num_rows:
            if (
                not cur_cell.has_bottom_wall
                and not self.__cells[col][down].visited
            ):
                cur_cell.draw_move(self.__cells[col][down])
                if self._solve_r(col, down):
                    return True
                cur_cell.draw_move(self.__cells[col][down], True)

        right = col + 1
        if right < self.__num_cols:
            if (
                not cur_cell.has_right_wall
                and not self.__cells[right][row].visited
            ):
                cur_cell.draw_move(self.__cells[right][row])
                if self._solve_r(right, row):
                    return True
                cur_cell.draw_move(self.__cells[right][row], True)
        
        left = col - 1
        if left >= 0:
            if (
                not cur_cell.has_left_wall
                and not self.__cells[left][row].visited
            ):
                cur_cell.draw_move(self.__cells[left][row])
                if self._solve_r(left, row):
                    return True
                cur_cell.draw_move(self.__cells[left][row], True)

        up = row - 1
        if up >= 0:
            if (
                not cur_cell.has_top_wall
                and not self.__cells[col][up].visited
            ):
                cur_cell.draw_move(self.__cells[col][up])
                if self._solve_r(col, up):
                    return True
                cur_cell.draw_move(self.__cells[col][up], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)
