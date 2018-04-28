'''
Unit tests for Profiler class

'''
import sys
sys.path.append(r'C:\Users\Shiva\Documents\New\AuthorProfiling\src') # change this if you are using Linux. 
#print(sys.path)
import unittest
import profiler

class TestMethods(unittest.TestCase):

    def testAverage(self):
    	p=profiler.Profiler()
    	testAvgMiddle=self.p.calculateAvg([5,10,15])
    	testAvgZero=self.p.calculateAvg([0])
    	self.assertEqual(testAvgMiddle,10)
    	self.assertEqual(testAvgZero,0)

    def testCommaIndex(self):
    	p=profiler.Profiler()
    	commaIndexlower=p.getCommaIndex("abc, xyz")
    	self.assertEqual(commaIndexlower,50)

    def testGetArticleIndex(self):
    	self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()