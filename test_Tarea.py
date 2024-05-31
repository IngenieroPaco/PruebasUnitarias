# Definición de las funciones para las operaciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: División por cero'

# Pruebas unitarias para las operaciones básicas
import unittest

class TestOperacionesBasicas(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(3, 2), 5)
        self.assertEqual(suma(-3, 2), -1)

    def test_resta(self):
        self.assertEqual(resta(3, 2), 1)
        self.assertEqual(resta(-3, 2), -5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 2), 6)
        self.assertEqual(multiplicacion(-3, 2), -6)

    def test_division(self):
        self.assertEqual(division(3, 2), 1.5)
        self.assertEqual(division(-3, 2), -1.5)

if __name__ == '__main__':
    unittest.main()
