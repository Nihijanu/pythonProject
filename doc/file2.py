import file1 as fs
import unittest
print(fs.name)
print(fs.version)
class myfile(unittest.TestCase):
    def test_sub(self):
        result=fs.sub(10,3)
        self.assertEqual(result,7)
    def test_add(self):
        result=fs.add(10,3)
        self.assertEqual(result,13)
    def test_mul(self):
        result=fs.mul(10,3)
        self.assertEqual(result,30)
if '__name__' == '__main__':
    unittest.main()