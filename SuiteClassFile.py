import unittest
from TestModule1 import TestMirror
from TestModule2 import TestMirrorSquared
from TestModSub import TestSub
from TestModTran import TestTran


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestMirror))
    suite.addTest(unittest.makeSuite(TestMirrorSquared))
    suite.addTest(unittest.makeSuite(TestSub))
    suite.addTest(unittest.makeSuite(TestTran))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()