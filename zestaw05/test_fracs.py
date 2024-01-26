import fracs
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertEqual(fracs.sub_frac([3, 4], [1, 2]), [1, 4])

    def test_mul_frac(self): 
        self.assertEqual(fracs.mul_frac([4, 5], [5, 6]), [2, 3])

    def test_div_frac(self): 
        self.assertEqual(fracs.div_frac([4, 5], [4, 5]), [1, 1])

    def test_is_positive(self): 
        self.assertTrue(fracs.is_positive([6, 5]))
        self.assertFalse(fracs.is_positive(self.zero))
        self.assertFalse(fracs.is_positive([0, 8]))
        self.assertFalse(fracs.is_positive([-1, 5]))
        self.assertFalse(fracs.is_positive([1, -5]))

    def test_is_zero(self): 
        self.assertTrue(fracs.is_zero(self.zero))
        self.assertTrue(fracs.is_zero([0, 9]))
        self.assertFalse(fracs.is_zero([3, 4]))

    def test_cmp_frac(self): 
        self.assertEqual(fracs.cmp_frac([1, 2], [5, 20]), -1)
        self.assertEqual(fracs.cmp_frac([1, 2], [5, 10]), 0)
        self.assertEqual(fracs.cmp_frac([1, 2], [5, 6]), 1)

    def test_frac2float(self): 
        self.assertAlmostEqual(fracs.frac2float([1, 3]), 0.3333333)
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)

    def tearDown(self): 
        pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy