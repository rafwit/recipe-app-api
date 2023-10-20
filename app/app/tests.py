"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """_summary_
        Test that two numbers are added together
        """
        self.assertEqual(calc.add(3,8), 11)
        
        
    def test_subsctract_numbers(self):
        """_summary_
        Test that values are subtracted and returned
        """
        self.assertEqual(calc.subtract(11,5), 6)