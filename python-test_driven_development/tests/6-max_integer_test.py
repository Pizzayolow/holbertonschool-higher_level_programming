#!/usr/bin/python3
"""UNITTEST OF MAX INTEGER
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_greater(self):
        """verify if the function work"""
        list = [10, 22, 11, 5, 1, 4, 7]
        self.assertEqual(max_integer(list), 22)
        
    def test_unique(self):
        """verify if the function work with 1 data"""
        list = [22]
        self.assertEqual(max_integer(list), 22)
        
    def test_dual(self):
        """verify with only two data"""
        list = [10, 22]
        self.assertEqual(max_integer(list), 22)
        
    def test_mirror(self):
        """verify if work with sames numbers"""
        list = [22, 22]
        self.assertEqual(max_integer(list), 22)
        
    def test_empty(self):
        """verify if works with empty list"""
        list = []
        self.assertIsNone(max_integer(list))
        
    def test_str(self):
        """verify if the function works with str"""
        list = ["Simon"]
        self.assertEqual(max_integer(list), "Simon")
        
    def test_neg(self):
        """verify with negatives numbers"""
        list = [-10, 22, 11, 5, -100, 4, 7]
        self.assertEqual(max_integer(list), 22)
        
    def test_floats(self):
        """verify with floats"""
        list = [10, 22.88, 11.5, 5, 1, 4, 7]
        self.assertEqual(max_integer(list), 22.88)

    def test_is_list(self):
        """verify if the list is a list"""
        data = [10, 22, 11, 5, 1, 4, 7]
        self.assertIsInstance(data, list)
        
    def test_is_int_or_float(self):
        """verify if the datas are int or floats"""
        data = [10, 22.88, 11, 88, 1, 4, 7]
        for element in range(len(data)):
            self.assertIsInstance(data[element], (int, float))
