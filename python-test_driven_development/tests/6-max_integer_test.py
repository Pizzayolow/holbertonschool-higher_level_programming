#!/usr/bin/python3
"""UNITTEST OF MAX INTEGER
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_greater(self):
        list = [10, 22, 11, 5, 1, 4, 7]
        self.assertEqual(max_integer(list), 22)
        
    def test_unique(self):
        list = [22]
        self.assertEqual(max_integer(list), 22)
        
    def test_dual(self):
        list = [10, 22]
        self.assertEqual(max_integer(list), 22)
        
    def test_mirror(self):
        list = [22, 22]
        self.assertEqual(max_integer(list), 22)
        
    def test_empty(self):
        list = []
        self.assertIsNone(max_integer(list))
        
    def test_str(self):
        list = ["Simon"]
        self.assertEqual(max_integer(list), "Simon")
        
    def test_neg(self):
        list = [-10, 22, 11, 5, -100, 4, 7]
        self.assertEqual(max_integer(list), 22)
        
    def test_floats(self):
        list = [10, 22.88, 11.5, 5, 1, 4, 7]
        self.assertEqual(max_integer(list), 22.88)

    def test_is_list(self):
        data = [10, 22, 11, 5, 1, 4, 7]
        self.assertIsInstance(data, list)
        
    def test_is_int_or_float(self):
        data = [10, 22.88, 11, 88, 1, 4, 7]
        for element in range(len(data)):
            self.assertIsInstance(data[element], (int, float))

if __name__ == '__main__':
    unittest.main()