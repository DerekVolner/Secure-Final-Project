import unittest
import BaseFileModProject6


class Test_TestMethods (unittest.TestCase):
    def test_putter(self):
        testArray=["a","b","c"]
        read=[]
        BaseFileModProject6.putter(testArray,read)
        self.assertEqual(read, ["a","b","c"])