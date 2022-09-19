#!/usr/bin/python3
'''Unittest for max_integer([..])'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Subclass for unittest for max_integer[..]'''
    
    def test_arranged_list(self):
        '''Test when list is arranged'''
        arranged = [5, 11, 17, 23, 31]
        self.assertEqual(max_integer(arranged), 31)

    def test_unarranged_list(self):
        '''Test when list is scattered'''
        scattered = [11, 31, 23, 5, 17]
        self.assertEqual(max_integer(scattered), 31)

    def test_empty_list(self):
        '''Test when list is empty []'''
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_single_string_list(self):
        '''Test for only one string as argument'''
        single = ["World"]
        with self.assertRaises(TypeError):
            max_integer(single)

    def test_mixed_string_int_list(self):
        '''Test for mixture of int and string in the list'''
        mixed = [5, 11, "World", 23, 31]
        with self.asserRaises(TypeError):
            max_integer(mixed)

    def test_all_floats(self):
        '''Test for only floats in the list'''
        flt = [5.5, -17.6, 23.7, 31.8, 11.9]
        self.assertAlmostEqual(max_integer(flt), 31.8)

    def test_ints_floats_list(self):
        '''Test when the list contains int and floats'''
        ifloat = [11, 5.5, -23, 31.6, 17]
        self.assertAlmostEqual(max_integer(ifloat), 31.6)

    def test_one_int_list(self):
        '''Test when the list has only one int'''
        one_int = [17]
        self.assertEqual(max_integer(one_int), 17)

    def test_max_beginning_list(self):
        '''Test when max int is at the beggining'''
        max_int_b = [31, 23, 17, 11, 5]
        self.assertEqual(max_integer(max_int_b), 31)

    def test_max_middle_list(self):
        '''Test when max int is at the middle'''
        max_int_m = [5, 11, 31, 17, 23]
        self.assertEqual(max_integer(max_int_m), 31)

    def test_empty_strings(self):
        '''Test for empty string'''
        empty_string = ""
        with self.assertRaises(TypeError):
            max_integer(empty_string)

    def test_no_arg(self):
        '''Test when no argument is passed'''
        self.assertIsNone(max_integer())

    def test_mixed_type(self):
        '''Test when list contains mixed types: int, float, string'''
        mix = [11, 5.5, "World", 23, 31.6]
        with self.assertRaises(TypeError):
            max_integer(mix)

    def test_string_group(self):
        '''Test for when the list contains only strings'''
        string_group = ["Emmanuel", "Please", "Bring", "Mat"]
        with self.assertRaises(TypeError):
            max_integer(string_group)

    def test_none(self):
        '''Test when None is passed as argument'''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_all_negative(self):
        '''Test when all int are less than zero'''
        neg = [-11, -17, -23, -5, -31]
        self.assertEqual(max_integer(neg), -5)

if __name__ == "__main__":
    unittest.main()
