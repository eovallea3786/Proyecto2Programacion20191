import unittest
import adn as f

class pruebas(unittest.TestCase):

    def test_obtener_complemento(self):
        self.assertEqual(f.obtener_complemento('A'), 'T')
        self.assertEqual(f.obtener_complemento('G'), 'C')
        self.assertEqual(f.obtener_complemento('T'), 'A')
        self.assertRaises(ValueError, f.obtener_complemento, 'Z')
    def test_generar_cadena_complementaria(self):
        self.assertEqual(f.generar_cadena_complementaria('ATGC'), 'TACG')
        self.assertEqual(f.generar_cadena_complementaria('GATC'), 'CTAG')
        self.assertEqual(f.generar_cadena_complementaria('CA'), 'GT')
    def test_calcular_correspondencia(self):
        self.assertEqual(f.calcular_correspondencia('ATATTACGGC', 'TATAATGCCG'), 100.0)
        self.assertEqual(f.calcular_correspondencia('ATATATCGGC', 'TATAATGCCG'),  80.0)
        self.assertEqual(f.calcular_correspondencia('ATATATCGGC', 'CGATTTACGA'), 20.0)
        self.assertEqual(f.calcular_correspondencia('TTGGAACC', 'ACTA'), 'Las cadenas no tienen la misma longitud')

