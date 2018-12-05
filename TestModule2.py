import unittest
from encryptor.encrysimple.mirrorsquared import MirrorSquared


class TestMirrorSquared(unittest.TestCase):
    
    @classmethod
    def setUPClass(cls):
        print("setupclass to run suite")
        
    def setUp(self): 
        self.t1 = MirrorSquared("DOG IS")#test for  all capitals
        self.t2 = MirrorSquared("DOG")# test for single word
        self.t3 = MirrorSquared("dog is mad")#test for  all lowercases
        self.t4 = MirrorSquared("dog 'he said' what")# sentence(s) with '' inside
        self.t5 = MirrorSquared("dog \ where has it gone") # sentence with \ inside 
        
    def tearDown(self):
        self.t1 = MirrorSquared("DOG IS")#test for  all capitals
        self.t2 = MirrorSquared("DOG")# test for single word
        self.t3 = MirrorSquared("dog is mad")#test for  all lowercases
        self.t4 = MirrorSquared("dog 'he said' what")# sentence(s) with '' inside
        self.t5 = MirrorSquared("dog \ where has it gone") # sentence with \ inside 

    def test_mirrorsquared(self):
        self.assertEqual(self.t1.text_revsquared(), 'S I   G O D')
        self.assertTrue(self.t2.text_revsquared(), 'G O D')
        self.assertEqual(self.t3.text_revsquared(), 'd a m   s i   g o d')
        self.assertEqual(self.t4.text_revsquared(), "t a h w   ' d i a s   e h '   g o d")
        self.assertEqual(self.t5.text_revsquared(),"e n o g   t i   s a h   e r e h w   \   g o d")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass to complete running suite")