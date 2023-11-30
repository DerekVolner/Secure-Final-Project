import unittest
import BaseFileModProject6
from BaseFileModProject6 import encrypt

class Test_TestMethods (unittest.TestCase):
    def test_FileName(self):
        self.assertRaises(FileNotFoundError)
        users_file == "test.txt"                
        encrypt()  