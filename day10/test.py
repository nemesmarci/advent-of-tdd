import unittest
from day10 import Maze


TEST_DATA_1 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]

AREA = {
    (0, 0): '.', (0, 1): '.', (0, 2): '.', (0, 3): '.', (0, 4): '.',
    (1, 0): '.', (1, 1): 'F', (1, 2): '-', (1, 3): '7', (1, 4): '.',
    (2, 0): '.', (2, 1): '|', (2, 2): '.', (2, 3): '|', (2, 4): '.',
    (3, 0): '.', (3, 1): 'L', (3, 2): '-', (3, 3): 'J', (3, 4): '.',
    (4, 0): '.', (4, 1): '.', (4, 2): '.', (4, 3): '.', (4, 4): '.',
}

LOOP = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]
DIRECTIONS = ['E', 'E', 'S', 'S', 'W', 'W', 'N', 'N']
START_PIPE_TEST = [
    (['.|.', '.S.', '.|.'], '|'),
    (['...', '-S-', '...'], '-'),
    (['.|.', '.S-', '...'], 'L'),
    (['.|.', '-S.', '...'], 'J'),
    (['...', '.S-', '.|.'], 'F'),
    (['...', '-S.', '.|.'], '7')
]

TEST_DATA_2 = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...'
]


class TestMaze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(TEST_DATA_1)

    def testParse(self):
        self.assertDictEqual(self.maze.area, AREA)
        self.assertEqual(self.maze.start, (1, 1))

    def testLoop(self):
        self.assertSetEqual(self.maze.loop(), set(LOOP))

    def testNextInLoop(self):
        for i in range(0, len(LOOP) - 1):
            self.assertEqual(self.maze.next_in_loop(LOOP[i], DIRECTIONS[i]),
                             (LOOP[i + 1], DIRECTIONS[i + 1]))

    def testStartPipeShape(self):
        for area, shape in START_PIPE_TEST:
            maze = Maze(area)
            self.assertEqual(maze.start_pipe_shape(), shape)

    def testPart1(self):
        self.assertEqual(self.maze.part_one(), 4)
        maze = Maze(TEST_DATA_2)
        self.assertEqual(maze.part_one(), 8)


if __name__ == '__main__':
    unittest.main()
