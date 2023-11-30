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
    def test_process(self):
        encryptedArray =["121a","121", "8", "121a" , "121a", "121a" , "4", "115", "108" ,"121a"]
        arrayDecrypted=[]
        BaseFileModProject6.process(encryptedArray,arrayDecrypted)
        self.assertEqual(arrayDecrypted,["y","z","\n", "y","y","y","\n", "z","t", "y" ] )
    def test_processEmptyString(self):
        emptyStringArray =['']
        arrayDecrypted=[]
        BaseFileModProject6.process(emptyStringArray,arrayDecrypted)
        self.assertEqual(emptyStringArray, [''])
    def test_EncryptNormal(self):
        plainText = "encryptFile.txt"
        encryptedText ="decryptFile.txt"
        run = BaseFileModProject6.encrypt2(plainText, encryptedText)
        self.assertEqual(run, "Encrypted passwords wrote to "+ encryptedText)
    def test_EncryptFileNotFound(self):
        plainText = "89897e.txt"
        encryptedText ="dededed.txt"
        run = BaseFileModProject6.encrypt2(plainText, encryptedText)
        self.assertEqual(run, "The text file you specified cannot be found")
    def test_decryptNormal(self):
        eString = "encryptFile.txt"
        dString = "decryptFile.txt"
        run = BaseFileModProject6.decrypt2(dString, eString)
        self.assertEqual(run, "Decrypted passwords wrote to "+ eString)
    def test_decryptFileNotFound(self):
        nonExistentFile ="doobee.txt"
        dString = "decryptFile.txt"
        run2 = BaseFileModProject6.decrypt2(nonExistentFile, dString)
        self.assertEqual(run2, "The text file you specified cannot be found")
    def test_decryptValueError(self):
        fileWithValueError = "valueError.txt"
        dString = "decryptFile.txt"
        run3 = BaseFileModProject6.decrypt2(fileWithValueError, dString)
        self.assertEqual(run3, "The values in the file have not been encrypted with this program")