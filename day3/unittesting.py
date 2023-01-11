import unittest
def sum(a,b):
    return a+b
class My_Test(unittest.TestCase):
    def test1(self):
        a=10
        b=20
        r=sum(a,b)
        self.assertEqual(r,30)
if "__name__"=="__main__":
    unittest.main()