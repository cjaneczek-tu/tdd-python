__author__ = 'uhs374h'
"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch import *


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testTuple(self):
        z, n = Bruch(3, 4)
        assert(z == 3 and n == 4)

    def testTuple2(self):
        z, n = self.b
        self.assertEqual(Bruch(z, n), self.b)

if __name__ == "__main__":
    unittest.main()