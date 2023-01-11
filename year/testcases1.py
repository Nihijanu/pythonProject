import login as l
import unittest
class my_File(unittest.TestCase):
    def test_l1(self):
        res=l.login("hcluser",1234)
        self.assertEqual(res,1)
    def test_l2(self):
        res=l.login("hclur",14)
        self.assertEqual(res,0)
if "__name__" == "__main__" :
    unittest.main()