import unittest
def mul(a,b):
    return a*b
class mytest(unittest.TestCase):
    def test1(self):
        p=mul(10,20)
        self.assertEqual(p,200)
    def test2(self):
        p=mul(20,10)
        self.assertEqual(p,200)
    def test3(self):
        p=mul(30,20)
        self.assertEqual(p,600)
    def test4(self):
        p=mul(10,5)
        self.assertEqual(p,50)
    def test5(self):
        p=mul(5,20)
        self.assertEqual(p,100)
if "__name__"== "__main__":
    unittest.main()