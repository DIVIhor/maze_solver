from sys import setrecursionlimit
import unittest

from maze import Maze


class Tests(unittest.TestCase):
    setrecursionlimit(5000)
    def test_maze_create_cells_small(self):
        num_cols = 6
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._Maze__cells), num_cols)
        self.assertEqual(len(maze._Maze__cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 50
        num_rows = 50
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._Maze__cells), num_cols)
        self.assertEqual(len(maze._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertFalse(maze._Maze__cells[0][0].has_top_wall)
        self.assertFalse(
            maze._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 7, 4, 10, 10)
        for col in range(maze._Maze__num_cols):
            for row in range(maze._Maze__num_rows):
                self.assertFalse(maze._Maze__cells[col][row].visited)


if __name__ == "__main__":
    unittest.main()
