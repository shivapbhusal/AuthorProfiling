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
    	testAvg=p.calculateAvg([5,10,15])
    	self.assertEqual(testAvg,10)

    def testCommaIndex(self):
    	self.assertEqual(1,1)

    def testGetArticleIndex(self):
    	self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()