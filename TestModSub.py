import unittest
from encryptor.encrycomplex.sub import Encr
from encryptor.encrycomplex.sub import Decr

class TestSub(unittest.TestCase):
    
    @classmethod
    def setUPClass(cls):
        print("setupclass to run suite")
        
    def setUp(self): 
        self.t1 = Encr("DOG IS",1)#test for  all capitals
        self.t2 = Encr("DOG",1)# test for single word
        self.t3 = Encr("dog is mad",1)#test for  all lowercases
        self.t4 = Encr("dog 'he said' what",1)# sentence(s) with '' inside
        self.t5 = Encr("dog \ where has it gone",1) # sentence with \ inside 
        
        self.t6 = Decr('EPH JT',1)#test for  all capitals
        self.t7 = Decr('EPH',1)# test for single word
        self.t8 = Decr('eph jt nbe',1)#test for  all lowercases
        self.t9 = Decr("eph (if tbje( xibu",1)# sentence(s) with '' inside
        self.t10 = Decr("eph ] xifsf ibt ju hpof",1) # sentence with \ inside 
        
        
    def tearDown(self):
        pass
    def test_mirrorsquared(self):
        self.assertEqual(self.t1.display(), 'EPH JT')
        self.assertTrue(self.t2.display(), 'EPH')
        self.assertEqual(self.t3.display(), 'eph jt nbe')
        self.assertEqual(self.t4.display(), "eph (if tbje( xibu")
        self.assertEqual(self.t5.display(),"eph ] xifsf ibt ju hpof")
        
        self.assertEqual(self.t6.display(), "DOG IS")
        self.assertTrue(self.t7.display(), "DOG")
        self.assertEqual(self.t8.display(), "dog is mad")
        self.assertEqual(self.t9.display(), "dog 'he said' what")
        self.assertEqual(self.t10.display(),"dog \ where has it gone")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass to complete running suite")
        
unittest.main(argv=[''], verbosity=2, exit=False) 