'''
Created on 5 sep 2011

@author: anders
'''
import unittest
import lekstuga

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testLeapyear(self):
        self.assertTrue(lekstuga.isLeapYear(2000))
        pass
    
    def testLeapyear100(self):
        self.assertFalse(lekstuga.isLeapYear(2100))
        pass

    def testLeapyearNormal(self):
        self.assertTrue(lekstuga.isLeapYear(2012))
        pass
    
    def testIsDate(self):
        self.assertTrue(lekstuga.isDate(2011, 9, 5))
        self.assertFalse(lekstuga.isDate(2011, 19, 5))
    
    def testConvertToNumbers(self):
        test = lekstuga.convertToNumbers("2011/01/12")
        
        self.assertTupleEqual(test, (2011,1,12))
        
    def testConvertToNumbersZeroYear(self):
        test = lekstuga.convertToNumbers("0/01/12")       
        self.assertTupleEqual(test, (0,1,12))
        
        test = lekstuga.convertToNumbers("00/01/12")        
        self.assertTupleEqual(test, (0,1,12))
        
    def testIsYear(self):
        self.assertTrue(lekstuga.isYear(0))
        self.assertTrue(lekstuga.isYear(99))
        self.assertFalse(lekstuga.isYear(10))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()