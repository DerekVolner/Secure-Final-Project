import unittest
import BaseFileModProject6


class Test_TestMethods (unittest.TestCase):
    def test_putter(self):
        testArray=["a","b","c"]
        read=[]
        BaseFileModProject6.putter(testArray,read)
        self.assertEqual(read, ["a","b","c"])
    def test_Conveter(self):
        filledArray=['z','y','\n','f','5','\n','e','\n','d','a','d','j']
        empty=[]
        BaseFileModProject6.Converter(empty,filledArray)
        self.assertEqual(empty,['122.','121a.','8.','99.','49.','5.','95.','3.','92.','88.','90.','95.'])
    def test_splitter(self):
        dottedArray = ["y.f.5.6.7.8.8.999.974.#.f"]
        empty =[]
        BaseFileModProject6.splitter(dottedArray, empty)
        self.assertEqual(empty,["y","f","5","6","7","8","8","999","974","#","f"])