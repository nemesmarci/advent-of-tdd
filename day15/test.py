import unittest
from day15 import Boxes

TEST_DATA = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
STRINGS = ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5','pc-', 'pc=6', 'ot=7']
HASHES = [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]


class TestBoxes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boxes = Boxes(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.boxes.strings, STRINGS)

    def testHash(self):
        for string, value in zip(STRINGS, HASHES):
            self.assertEqual(self.boxes.hash(string), value)


if __name__ == '__main__':
    unittest.main()
