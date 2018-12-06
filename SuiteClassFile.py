{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_mirror (TestModule1.TestMirror) ... ok\n",
      "test_mirrorsquared (TestModule2.TestMirrorSquared) ... ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 2 tests in 0.002s\n",
      "\n",
      "OK\n",
      "test_mirror (TestModule1.TestMirror) ... ok\n",
      "test_mirrorsquared (TestModule2.TestMirrorSquared) ... ok\n",
      "test_mirrorsquared (TestModSub.TestSub) ... ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 3 tests in 0.005s\n",
      "\n",
      "OK\n",
      "...."
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "teardownclass to complete running suite\n",
      "<unittest.runner.TextTestResult run=4 errors=0 failures=0>\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 4 tests in 0.017s\n",
      "\n",
      "OK\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "from TestModule1 import TestMirror\n",
    "from TestModule2 import TestMirrorSquared\n",
    "from TestModSub import TestSub\n",
    "from TestModTran import TestTran\n",
    "\n",
    "\n",
    "def my_suite():\n",
    "    suite = unittest.TestSuite()\n",
    "    result = unittest.TestResult()\n",
    "    suite.addTest(unittest.makeSuite(TestMirror))\n",
    "    suite.addTest(unittest.makeSuite(TestMirrorSquared))\n",
    "    suite.addTest(unittest.makeSuite(TestSub))\n",
    "    suite.addTest(unittest.makeSuite(TestTran))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
