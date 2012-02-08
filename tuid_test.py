'''
@author: Alex Decker
'''

import unittest
import tuid

class TestSequenceFunctions(unittest.TestCase):

    def test_normal(self):
        tuid.tuid_init(874733474, 4)
        str = tuid.tuid(324)
        self.assertIsNotNone(str)
        
    def test_displaysequence(self):
        tuid.tuid_init(764544738374, 4)   
        for i in range(80):
            print tuid.tuid(i),
            if i%20 == 0:print
        print
        
    def test_crossSession(self):
        """ tests to make sure that the same identifier is produced
            for a given seed/other inputs.
        """
        tuid.tuid_init(874738374, 3)
        a = tuid.tuid(42)
        tuid.tuid_init(874738374, 3)      
        b = tuid.tuid(42)
         
        self.assertEqual(a, b)
        
    def test_changeLength(self):
        """ tests to make sure that a new key is generated when the length is changed 
        """
        #TODO
        
    def test_coverage(self):
        length = 3
        tuid.tuid_init(None, length)  
        
        alph = tuid.defaultAlphabet
        seen = set()
        dup = []
        for i in range(0,pow(len(alph),length)):
            if i % pow(2,14) == 0: print i
            s = tuid.tuid(i)
            if s in seen:
                print i,s
                dup.append(s)
            else:
                seen.add(s)
        self.assertListEqual(dup,[])

if __name__ == '__main__':
    unittest.main()
