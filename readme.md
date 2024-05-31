# Primero, definimos las funciones para las operaciones básicas.

# La función 'suma' toma dos números como argumentos (a y b) y devuelve su suma.
def suma(a, b):
    return a + b

# La función 'resta' toma dos números como argumentos (a y b) y devuelve la resta del primero menos el segundo.
def resta(a, b):
    return a - b

# La función 'multiplicacion' toma dos números como argumentos (a y b) y devuelve su producto.
def multiplicacion(a, b):
    return a * b

# La función 'division' toma dos números como argumentos (a y b).
# Primero, verifica si el segundo número es cero para evitar una división por cero.
# Si el segundo número no es cero, devuelve la división del primero entre el segundo.
# Si el segundo número es cero, devuelve un mensaje de error.
def division(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: División por cero'

# Ahora, vamos a realizar pruebas unitarias para las operaciones básicas.
# Para esto, importe el módulo 'unittest' de Python.
import unittest

# Defino una clase 'TestOperacionesBasicas' que hereda de 'unittest.TestCase'.
# Dentro de esta clase, voy a definir varios métodos, cada uno de los cuales realizará una prueba unitaria.
class TestOperacionesBasicas(unittest.TestCase):

# Este método prueba la función 'suma'.
    def test_suma(self):
# Use 'assertEqual' para verificar que el resultado de 'suma(3, 2)' es igual a 5.
        self.assertEqual(suma(3, 2), 5)
# Hare otra prueba con números negativos.
        self.assertEqual(suma(-3, 2), -1)

# Este método prueba la función 'resta'.
    def test_resta(self):
        self.assertEqual(resta(3, 2), 1)
# Igual que el anterior hare otra prueba pero con numeros negativos.
        self.assertEqual(resta(-3, 2), -5)

 # Este método prueba la función 'multiplicacion'.
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 2), 6)
        self.assertEqual(multiplicacion(-3, 2), -6)

# Este método prueba la función 'division'.
    def test_division(self):
        self.assertEqual(division(3, 2), 1.5)
        self.assertEqual(division(-3, 2), -1.5)

# Esta línea verifica si este archivo se está ejecutando directamente.
# Si es así, ejecuta las pruebas unitarias.
# Si este archivo se está importando desde otro archivo, no ejecuta las pruebas.
if __name__ == '__main__':
    unittest.main()


# -------------- INFORME DE COBERTURA --------------
Ran 4 tests in 0.002s

OK
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
test_Tarea.py      26      2    92%   15, 39
---------------------------------------------
TOTAL              26      2    92%

# Este es el informe de cobertura dada por la libreria coverage, a continuacion explicare que significa cada cosa dada en el informe

# Ran 4 tests in 0.002s: Esto significa que se ejecutaron 4 pruebas (una para cada operación matemática) y que todas se completaron en 0.002 segundos.
# OK: Esto indica que todas las pruebas pasaron sin errores ni fallas.
# Name: Este es el nombre del archivo que se probó.
# Stmts: Este es el número total de “declaraciones” en mi archivo. Una declaración es básicamente cualquier línea de código que hace algo.
# Miss: Este es el número de declaraciones que no se ejecutaron durante las pruebas. En mi caso, hay 2 declaraciones que no se ejecutaron.
# Cover: Este es el porcentaje de tu código que fue cubierto por las pruebas. En mi caso, el 92% de tu código fue cubierto por las pruebas.
# Missing: Estas son las líneas específicas del código que no se ejecutaron durante las pruebas. En mi caso, las líneas 15 y 39 no se ejecutaron, pero naturalmente el codigo escrito en esas lineas no se ejecutan en las pruebas <3.