import random
import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    def test1(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test2(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test3(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test4(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test5(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test6(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')
    def test7(self):
        val = 155
        self.assertFalse(contrived_func(val), msg='incorrect')


if __name__ == '__main__':
    unittest.main()
