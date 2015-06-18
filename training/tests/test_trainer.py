__author__ = 'liz'

import unittest
from training.trainer import Trainer


class TestOutbrainTrainer(unittest.TestCase):
    def setUp(self):
        self.q_file = '../data/query_groups.txt'
        self.i_file = '../data/input_groups_2.txt'
        self.tr = Trainer()

    def test_read_file(self):
        data = self.tr.read_file(self.q_file)
        self.assertEqual(type(data), list)
        for line in data:
            self.assertEqual(type(line), list)
            for word in line:
                self.assertEqual(type(word), str)

    def test_output(self):
        data = {"blue": 1, "red": 2, "yellow": 1}
        result = self.tr.output(data)
        self.assertEqual(type(result), str)

    def test_get_query(self):
        results = self.tr.get_query(self.q_file)
        for r in results:
            self.assertEqual(type(r), set)

    def test_get_inputs(self):
        results = self.tr.get_query(self.i_file)
        for r in results:
            self.assertEqual(type(r), set)

    def test_match_query_input(self):
        results = self.tr.match_query_input(self.i_file, self.q_file)
        self.assertEqual(type(results), str)

if __name__ == '__main__':
    unittest.main()
