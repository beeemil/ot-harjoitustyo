import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_saldo_vahenee_oikein_kun_rahaa_on(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)
        
    def test_saldo_ei_muutu_kun_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_palauttaa_true_kun_saldo_riittaa(self):
        ret = self.maksukortti.ota_rahaa(5)
        self.assertEqual(ret, True)

    def test_palauttaa_false_kun_saldo_ei_riita(self):
        ret = self.maksukortti.ota_rahaa(20)
        self.assertEqual(ret, False)
    
    def test_string_toimii(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")