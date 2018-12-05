import unittest
from encryptor.encrysimple.mirror import Mirror


class TestMirror(unittest.TestCase):
    
    @classmethod
    def setUPClass(cls):
        print("setupclass to run suite")
        
    def setUp(self): 
        self.t1 = Mirror("DOG IS")#test for  all capitals
        self.t2 = Mirror("DOG")# test for single word
        self.t3 = Mirror("dog is mad")#test for  all lowercases
        self.t4 = Mirror("dog 'he said' what")# sentence(s) with '' inside
        self.t5 = Mirror("dog \ where has it gone") # sentence with \ inside 
        
    def tearDown(self):
        self.t1 = Mirror("DOG IS")#test for  all capitals
        self.t2 = Mirror("DOG")# test for single word
        self.t3 = Mirror("dog is mad")#test for  all lowercases
        self.t4 = Mirror("dog 'he said' what")# sentence(s) with '' inside
        self.t5 = Mirror("dog \ where has it gone") # sentence with \ inside 

    def test_mirror(self):
        self.assertEqual(self.t1.text_revmirror(), 'IS DOG')
        self.assertTrue(self.t2.text_revmirror(), 'DOG')
        self.assertEqual(self.t3.text_revmirror(), 'mad is dog')
        self.assertTrue(self.t4.text_revmirror(), "what 'said he' dog")
        self.assertEqual(self.t5.text_revmirror(),"gone it has where \ dog")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass to complete running suite")
  
