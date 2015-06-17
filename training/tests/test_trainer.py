__author__ = 'liz'

import unittest
from training.trainer import Trainer


class TestOutbrainTrainer(unittest.TestCase):
    def setUp(self):
        self.q_file = '../data/query_groups.txt'
        self.i_file = '../data/input_groups.txt'


    def test_read_file_returns_list(self):
        tr = Trainer()
        data = tr.read_file(self.q_file)
        self.assertEqual(type(data), list)

    def test_output(self):
        tr = Trainer()
        data = {"blue": 1, "red": 2, "yellow": 1}
        result = tr.output(data)
        self.assertEqual(type(result), str)

if __name__ == '__main__':
    unittest.main()
