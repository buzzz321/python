import unittest
import alternate,datetime

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testLowestDate(self):
        self.assertEqual(datetime.date(2001,2,3), alternate.lowestDate("1/2/3"))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
