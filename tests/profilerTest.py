'''
Unit tests for Profiler class

'''
import sys
sys.path.insert(1, '/home/civaist/Desktop/AuthorProfiling/src/profiler.py')
import unittest
import profiler

class TestMethods(unittest.TestCase):

    def test_upper(self):
    	p=profiler.Profiler()
    	testAvg=p.calculateAvg([5,10,15])
    	self.assertEqual(testAvg,10)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
    	self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()