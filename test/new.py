import unittest
def append(l,r):
    l.append(r)
    return l
def reverse(l):
    l.reverse()
    return l
class Mytest(unittest.TestCase):
    def test1(self):
        l=[10,20,30,40]
        r=50
        p=append(l,r)
        self.assertEqual(p,[10,20,30,40,50])

    def test2(self):
        l = [10, 20, 30, 40]
        p = reverse(l)
        self.assertEqual(p, [40,30,20,10])
if "__name__"=="__main__":
    unittest.main()

