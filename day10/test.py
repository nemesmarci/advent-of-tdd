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

ENCLOSED_3 = {(6, 2), (6, 3), (6, 7), (6, 8)}

MAZE_4 = [
    '..........',
    '.S------7.',
    '.|F----7|.',
    '.||....||.',
    '.||....||.',
    '.|L-7F-J|.',
    '.|..||..|.',
    '.L--JL--J.',
    '..........'
]

ENCLOSED_4 = {(6, 2), (6, 3), (6, 6), (6, 7)}

MAZE_5 = [
    '.F----7F7F7F7F-7....',
    '.|F--7||||||||FJ....',
    '.||.FJ||||||||L7....',
    'FJL7L7LJLJ||LJ.L-7..',
    'L--J.L7...LJS7F-7L7.',
    '....F-J..F7FJ|L7L7L7',
    '....L7.F7||L7|.L7L7|',
    '.....|FJLJ|FJ|F7|.LJ',
    '....FJL-7.||.||||...',
    '....L---J.LJ.LJLJ...'
]

ENCLOSED_5 = {(3, 14), (4, 7), (4, 8), (4, 9), (5, 7), (5, 8), (6, 6), (6, 14)}


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
        self.assertSetEqual(self.maze.enclosed_tiles(), ENCLOSED_3)

    def testPart2(self):
        self.assertEqual(self.maze.part_two(), 4)


class TestMaze4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(MAZE_4)

    def testEnclosed(self):
        self.assertSetEqual(self.maze.enclosed_tiles(), ENCLOSED_4)

    def testPart2(self):
        self.assertEqual(self.maze.part_two(), 4)


class TestMaze5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = Maze(MAZE_5)

    def testEnclosed(self):
        self.assertSetEqual(self.maze.enclosed_tiles(), ENCLOSED_5)

    def testPart2(self):
        self.assertEqual(self.maze.part_two(), 8)


if __name__ == '__main__':
    unittest.main()
