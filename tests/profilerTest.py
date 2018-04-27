'''
Unit tests for Profiler class

'''
import sys
sys.path.insert(1, '/home/civaist/Desktop/AuthorProfiling/src/profiler.py')
import unittest
import profiler

class TestMethods(unittest.TestCase):

    def testAverage(self):
    	p=profiler.Profiler()
    	testAvg=p.calculateAvg([5,10,15])
    	self.assertEqual(testAvg,10)

if __name__ == '__main__':
    unittest.main()