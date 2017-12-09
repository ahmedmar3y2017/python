from __future__ import print_function

import unittest

def add(x,y):
    return x+y

# Test Case Class 
class ExponentCalcTest(unittest.TestCase):
    # Function Success 
    def testSuccess(self):
        result=add(10,10)
        self.assertEqual(result , 20)
        #function Failure
    def testfailure(self):
        result=add(10,10)
        self.assertNotEqual(result , 100)



# Test
unittest.main()





