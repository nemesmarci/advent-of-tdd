import unittest
from day10 import Maze


TEST_DATA = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]

AREA = {
    (0, 0): '.', (0, 1): '.', (0, 2): '.', (0, 3): '.', (0, 4): '.',
    (1, 0): '.', (1, 1): 'S', (1, 2): '-', (1, 3): '7', (1, 4): '.',
    (2, 0): '.', (2, 1): '|', (2, 2): '.', (2, 3): '|', (2, 4): '.',
    (3, 0): '.', (3, 1): 'L', (3, 2): '-', (3, 3): 'J', (3, 4): '.',
    (4, 0): '.', (4, 1): '.', (4, 2): '.', (4, 3): '.', (4, 4): '.',
}

LOOP = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)}


class TestMaze(unittest.TestCase):
    def testParse(self):
        maze = Maze(TEST_DATA)
        self.assertDictEqual(maze.area, AREA)
        self.assertEqual(maze.start, (1, 1))

    def testLoop(self):
        maze = Maze(TEST_DATA)
        self.assertSetEqual(maze.loop(), LOOP)


if __name__ == '__main__':
    unittest.main()
