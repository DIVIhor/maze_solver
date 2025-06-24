from sys import setrecursionlimit, argv
from time import sleep

from graphics import Window
from maze import Maze


def main():
    setrecursionlimit(5000)
    win_width: int = 1080
    win_height: int = 1080
    margin: int = 50
    columns: int = 20
    rows: int = 20
    delay: int = 0

    # user could set whether 0, 1 or 3 arguments
    # 1 = a delay in seconds before script try to solve the generated maze
    # 3 = a delay in seconds, a number of columns, and a number of rows
    arguments: list[str] = argv
    if len(arguments) >= 2:
        delay_entry: int = int(arguments[1])
        # set a 120 seconds limit
        if 0 < delay_entry < 120:
            delay = delay_entry
        elif delay_entry >= 120:
            delay = 120
    if len(arguments) == 4:
        # 50x50 max grid size
        columns_entry: int = int(arguments[2])
        if 3 < columns_entry < 50:
            columns = columns_entry
        elif columns_entry >= 50:
            columns = 50
        rows_entry: int = int(arguments[3])
        if 3 < rows_entry < 50:
            rows = rows_entry
        elif rows_entry >= 50:
            rows = 50

    cell_width = (win_width - 2 * margin) // columns
    cell_height = (win_height - 2 * margin) // rows

    win = Window(win_width, win_height)
    maze = Maze(margin, margin, rows, columns, cell_width, cell_height, win)
    print("Maze created")

    # give user time to solve the maze
    if delay > 0:
        sleep(delay)

    # solve the maze and print a brief report
    is_solvable = maze.solve()
    if is_solvable:
        print("Maze solved!")
    else:
        print("Maze cannot be solved!")

    win.wait_for_close()


if __name__ == "__main__":
    main()