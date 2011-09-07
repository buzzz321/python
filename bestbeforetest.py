'''
Created on 5 sep 2011

@author: anders
'''
import unittest
import bestbefore

class Test(unittest.TestCase):


  def setUp(self):
    pass


  def tearDown(self):
    pass


  def testLeapyear(self):
    self.assertTrue(bestbefore.isLeapYear(2000))
    pass

  def testLeapyear100(self):
    self.assertFalse(bestbefore.isLeapYear(2100))
    pass

  def testLeapyearNormal(self):
    self.assertTrue(bestbefore.isLeapYear(2012))
    pass

  def testIsDate(self):
    self.assertTrue(bestbefore.isDate(2011, 9, 5))
    self.assertFalse(bestbefore.isDate(2011, 19, 5))

  def testConvertToNumbers(self):
    test = bestbefore.convertToNumbers("2011/01/12")

    self.assertListEqual(test, [2011,1,12])

  def testConvertToNumbersZeroYear(self):
    test = bestbefore.convertToNumbers("0/01/12")       
    self.assertListEqual(test, [0,1,12])

    test = bestbefore.convertToNumbers("00/01/12")        
    self.assertListEqual(test, [0,1,12])

  def testIsYear(self):
    self.assertTrue(bestbefore.isYear(0))
    self.assertTrue(bestbefore.isYear(99))
    self.assertFalse(bestbefore.isYear(10))

  def testLowestDate(self):
    self.assertListEqual(bestbefore.lowestDate([1,2,3]), [2001,2,3])
    self.assertListEqual(bestbefore.lowestDate([3,2,1]), [2001,2,3])

  def testLowestDate1000(self):
    self.assertListEqual(bestbefore.lowestDate([3,2002,1]), [2002,1,3])

  def testLowestDateSP2(self):
    self.assertListEqual(bestbefore.lowestDate([31,9,73]), [0,0,0])


  def testLowestDateSP1(self):
    self.assertListEqual(bestbefore.lowestDate([2,4,67]), [2067,2,4])
if __name__ == "__main__":
  #import sys;sys.argv = ['', 'Test.testName']
  unittest.main()
