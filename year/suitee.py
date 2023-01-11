import unittest
from testcases import my_file
from testcases1 import my_File
def mysuite():
    suite=unittest.TestSuite()
    res=unittest.TestResult()
    suite.addTests(unittest.makeSuite(my_file))
    suite.addTests(unittest.makeSuite(my_File))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
mysuite()
