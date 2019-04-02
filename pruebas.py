import unittest
import adn as f

class pruebas(unittest.TestCase):

    def test_obtener_complemento(self):
        self.assertEqual(f.obtener_complemento('A'), 'T')
        self.assertEqual(f.obtener_complemento('G'), 'C')
        self.assertEqual(f.obtener_complemento('T'), 'A')
        self.assertRaises(ValueError, f.obtener_complemento, 'Z')
    def test_generar_cadena_complementaria(self):
        self.ass