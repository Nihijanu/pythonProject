import code as c
import unittest
class my_file(unittest.TestCase):
    def test_m1(self):
        result=c.count_days(1)
        self.assertEqual(result,31)
    def test_m2(self):
        result=c.count_days(2)
        self.assertEqual(result,28)
    def test_m3(self):
        result=c.count_days(3)
        self.assertEqual(result,31)
    def test_m4(self):
        result=c.count_days(4)
        self.assertEqual(result,30)
    def test_m5(self):
        result=c.count_days(5)
        self.assertEqual(result,31)
    def test_m6(self):
        result=c.count_days(6)
        self.assertEqual(result,30)
    def test_m7(self):
        result=c.count_days(7)
        self.assertEqual(result,31)
    def test_m8(self):
        result=c.count_days(8)
        self.assertEqual(result,31)
    def test_m9(self):
        result=c.count_days(9)
        self.assertEqual(result,30)
    def test_m10(self):
        result=c.count_days(10)
        self.assertEqual(result,31)
    def test_m11(self):
        result=c.count_days(11)
        self.assertEqual(result,30)
    def test_m12(self):
        result=c.count_days(12)
        self.assertEqual(result,31)
if '__name__' =='__main__':
    unittest.main()