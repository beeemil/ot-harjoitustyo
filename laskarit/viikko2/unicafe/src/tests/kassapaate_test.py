import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti_low = Maksukortti(230)

    def test_kassapaatteen_rahamaara_ja_myydyt_lounaat_oikein(self):
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(lounaat, 0)
    
    def test_riittava_maksu_lisaa_edullisten_lounaiden_maaraa_ja_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittava_maksu_lisaa_maukkaiden_lounaiden_maaraa_ja_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_ei_riittava_maksu_ei_muuta_maukkaiden_lounaiden_maaraa_ja_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(380)
        self.assertEqual(vaihtoraha, 380)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_ei_riittava_maksu_ei_muuta_edulliset_lounaiden_maaraa_ja_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_lounas_onnistuu_kortilla(self):
        check = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(check, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_onnistuu_kortilla(self):
        check = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(check, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_lounas_ei_onnistu_kortilla(self):
        check = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_low)
        self.assertEqual(check, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksukortti_low.saldo, 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_ei_onnistu_kortilla(self):
        check = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_low)
        self.assertEqual(check, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti_low.saldo, 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_negatiivisella_latauksella_ei_tapahdu_mitaan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)