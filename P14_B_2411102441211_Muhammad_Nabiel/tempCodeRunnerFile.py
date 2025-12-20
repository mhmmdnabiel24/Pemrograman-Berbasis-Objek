import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_float(self):
        # Tes 5: Diskon 33% dari 999 = 669.33
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_awal_nol(self):
        # Tes 6: Harga awal 0
        hasil = self.calc.hitung_diskon(0, 10)
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()