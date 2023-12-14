import unittest
from day10 import Maze


MAZE_1 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]

ZOOM_1 = [
    "...............",
    "...............",
    "...............",
    "...............",
    "....S-----7....",
    "....|.....|....",
    "....|.....|....",
    "....|.....|....",
    "....|.....|....",
    "....|.....|....",
    "....L-----J....",
    "...............",
    "...............",
    "...............",
    "...............",
]

AREA = {
    (0, 0): '.', (0, 1): '.', (0, 2): '.', (0, 3): '.', (0, 4): '.',
    (1, 0): '.', (1, 1): 'F', (1, 2): '-', (1, 3): '7', (1, 4): '.',
    (2, 0): '.', (2, 1): '|', (2, 2): '.', (2, 3): '|', (2, 4): '.',
    (3, 0): '.', (3, 1): 'L', (3, 2): '-', (3, 3): 'J', (3, 4): '.',
    (4, 0): '.', (4, 1): '.', (4, 2): '.', (4, 3): '.', (4, 4): '.',
}

LOOP_1 = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]
DIRECTIONS_1 = ['E', 'E', 'S', 'S', 'W', 'W', 'N', 'N']
START_PIPE_TEST = [
    (['.|.', '.S.', '.|.'], '|'),
    (['...', '-S-', '...'], '-'),
    (['.|.', '.S-', '...'], 'L'),
    (['.|.', '-S.', '...'], 'J'),
    (['...', '.S-', '.|.'], 'F'),
    (['...', '-S.', '.|.'], '7')
]

MAZE_2 = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...'
]

MAZE_3 = [
    '...........',
    '.S-------7.',
    '.|F-----7|.',
    '.||.....||.',
    '.||.....||.',
    '.|L-7.F-J|.',
    '.|..|.|..|.',
    '.L--J.L--J.',
    '...........'
]

ENCLOSED_1 = {(6, 2), (6, 3), (6, 7), (6, 8)}


class TestMaze1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(MAZE_1)

    def testParse(self):
        self.assertDictEqual(self.maze.area, AREA)
        self.assertEqual(self.maze.start, (1, 1))

    def testLoop(self):
        self.assertSetEqual(self.maze.loop(), set(LOOP_1))

    def testNextInLoop(self):
        for i in range(0, len(LOOP_1) - 1):
            self.assertEqual(self.maze.next_in_loop(LOOP_1[i], DIRECTIONS_1[i]),
                             (LOOP_1[i + 1], DIRECTIONS_1[i + 1]))

    def testPart1(self):
        self.assertEqual(self.maze.part_one(), 4)

    def testZoom(self):
        expected = Maze(ZOOM_1).loop()
        self.assertSetEqual(self.maze.zoom(), expected)


class TestMaze2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(MAZE_2)

    def testPart1(self):
        self.assertEqual(self.maze.part_one(), 8)


class TestUniqueMaze(unittest.TestCase):
    def testStartPipeShape(self):
        for area, shape in START_PIPE_TEST:
            maze = Maze(area)
            self.assertEqual(maze.start_pipe_shape(), shape)


class TestMaze3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(MAZE_3)

    def testEnclosed(self):
        self.assertSetEqual(self.maze.enclosed_tiles(), ENCLOSED_1)


if __name__ == '__main__':
    unittest.main()
