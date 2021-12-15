########################################################################
##
## CS 101 Lab
## Program 13
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : unit testing
##
##      
##      
########################################################################

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):

        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")

    def test_total_returns_0(self):

        result2 = Grades.total([])
        self.assertEqual(result2,0,"The total function should return 0")

    def test_average_one(self):

        result3 = Grades.average([2,5,9])
        self.assertAlmostEqual(result3,5.333,3,"The average function should return 5.333")
    
    def  test_average_two(self):

        result4 = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result4,12.0000,4,"The average function should return 12.0000")

    def test_average_returns_nan(self):

        result5 = Grades.average([])
        self.assertIs(result5,math.nan,"The average funtion should return 'math.nan'")

    def test_median_one(self):

        result6 = Grades.median([2,5,1])
        self.assertEqual(result6,2,"The median function should return 2")

    def test_median_two(self):

        result7 = Grades.median([5, 2, 1, 3])
        self.assertEqual(result7,2.5,'The median function should return 2.5')

    def test_median_returns_ValueError(self):

        with self.assertRaises(ValueError):
            result = Grades.median([])

unittest.main()