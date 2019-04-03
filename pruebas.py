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
    def test_corresponden(self):
        self.assertTrue(f.corresponden('A', 'T'), True)
        self.assertFalse(f.corresponden('G', 'T'), False)
    def test_es_cadena_valida(self):
        self.assertFalse(f.es_cadena_valida('FTATTACGGC'), False)
        self.assertTrue(f.es_cadena_valida('ATATTACGGC'), True)
    def test_es_base(self):
        self.assertTrue(f.es_base('A'), True)
        self.assertTrue(f.es_base('T'), True)
        self.assertTrue(f.es_base('G'), True)
        self.assertTrue(f.es_base('C'), True)
        self.assertFalse(f.es_base('B'), False)
    def test_es_subcadena(self):
        self.assertTrue(f.es_subcadena('ATCTTA', 'ATC'), True)
        self.assertFalse(f.es_subcadena('TCGA', 'AAT'), False)
    def test_reparar_dano(self):
        self.assertEqual(f.reparar_dano('ATGPPP', 'C'), 'ATGPPP')
        self.assertEqual(f.reparar_dano('ATGCCC', 'G'), 'ATGCCC')
    def test_obtener_secciones(self):
        self.assertEqual(f.obtener_secciones('atata', 3), ['a', 't', 'ata'])
        self.assertEqual(f.obtener_secciones('ATGCTACAG', 2), ['ATGC', 'TACAG'])
    def  test_obtener_complementos(self):
        self.assertEqual(f.obtener_complementos(['AAA', 'CGC']), ['TTT', 'GCG'])
        self.assertEqual(f.obtener_complementos(['AGT', 'GTA']), ['TCA', 'CAT'])
    def test_unir_cadena(self):
        self.assertEqual(f.unir_cadena(['CGTA', 'ATTA']), 'CGTAATTA')
        self.assertEqual(f.unir_cadena(['GC', 'GCATTT']), 'GCGCATTT')
    def test_complementar_cadenas(self):
        self.assertEqual(f.complementar_cadenas(['GCC', 'CGG']), 'CGGGCC')
        self.assertEqual(f.complementar_cadenas(['AT', 'GTA', 'CC']), 'TACATGG')




