import unittest
from encryptor.encrycomplex.tran import tran

class TestTran(unittest.TestCase):
    
    @classmethod
    def setUPClass(cls):
        print("setupclass to run suite")
        
    def setUp(self): 
        self.t1 = tran("DOG IS")#test for  all capitals
        self.t2 = tran("DOG")# test for single word
        self.t3 = tran("dog is mad")#test for  all lowercases
        self.t4 = tran("dog 'he said' what")# sentence(s) with '' inside
        self.t5 = tran("dog \ where has it gone") # sentence with \ inside 
        
    def tearDown(self):
        pass
    def test_mirror(self):
        self.assertEqual(self.t1, tran('DOG IS'))
        self.assertTrue(self.t2, tran("DOG"))
        self.assertEqual(self.t3, tran("dog is mad"))
        self.assertTrue(self.t4, tran("dog 'he said' what"))
        self.assertEqual(self.t5, tran("dog \ where has it gone"))
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass to complete running suite")
        
unittest.main(argv=[''], verbosity=2, exit=False)