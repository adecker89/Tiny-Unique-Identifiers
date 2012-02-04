'''
Created on Feb 3, 2012

@author: alex
'''

import random
import unittest
import tuid

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_normal(self):
        str = tuid.tuid(324,4)
        self.assertIsNotNone(str)       

if __name__ == '__main__':
    unittest.main()
