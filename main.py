from sys import setrecursionlimit
from time import sleep

from graphics import Window
from maze import Maze


def main():
    setrecursionlimit(5000)
    win_width = 1080
    win_height = 1080
    margin = 50
    columns = 20
    rows = 20
    cell_width = (win_width - 2 * margin) // columns
    cell_height = (win_height - 2 * margin) // rows

    win = Window(win_width, win_height)
    maze = Maze(margin, margin, rows, columns, cell_width, cell_height, win)
    print("Maze created")

    sleep(10)  # 10s delay to give a chance to solve puzzle
    is_solvable = maze.solve()
    if is_solvable:
        print("Maze solved!")
    else:
        print("Maze cannot be solved!")

    win.wait_for_close()


if __name__ == "__main__":
    main()