# -*- coding: utf-8 -*-
"""
@author: nadime
"""
import unittest

from act7_1_numeros import Racionales

class TestRacionalesMethods(unittest.TestCase):
    
    def test_print_hello(self):
        r = Racionales(2.5)
        self.assertEqual(r.print_hello(), "Hola, soy un número racional.")

if __name__ == '__main__':
    unittest.main()