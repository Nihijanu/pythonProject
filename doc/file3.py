import unittest
from file2 import myfile
def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestSuite()
    suite.addTests(unittest.makeSuite(myfile))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()