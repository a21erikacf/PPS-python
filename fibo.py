import unittest

# Función fibonacci
def fibonacci(veces):

    contador = 1
    num1 = 0
    num2 = 1

    # Lista con la secuencia
    secuencia_fibonacci = [num1]
    
    while (contador < veces):

        numresultado = num1
        num1 = num2
        num2 = num1 + numresultado
        
        contador += 1
        # Añade el número calculado a la lista
        secuencia_fibonacci.append(num1)

    # Se muestra por pantalla la secuencia de números
    print(secuencia_fibonacci)
    # Y se devuelve la misma, para que se pueda usar en la prueba
    return secuencia_fibonacci

# Función comprobar valor en posición
def fibonacci_posicion(numpos):
    if numpos <= 0:
        return "Se debe indicar un número igual o mayor a 0."
    elif numpos == 1:
        return 0
    elif numpos == 2:
        return 1
    else:
        num1, num2 = 0, 1
        for _ in range(numpos - 2):
            num1, num2 = num2, num1 + num2
        return num2

# Función comprobación con Unitest
class TestFibonacci(unittest.TestCase):

    # Función de prueba
    def test_quinta_posicion(self):
        # Preguntamos la posición que se quiere comprobar
        posicion = int(input("Indica el número de la posición de la sucesión de Fibonacci que deseas comprobar: "))
        
        try:
            # Realizamos la secuencia Fibonacci con la posición a calcular
            secuencia = fibonacci(posicion)
            # Y calculamos el valor correspondiente a la posición con la función
            valor_posicion = fibonacci_posicion(posicion)
            # Verificamos si la quinta posición de la secuencia de Fibonacci es 3
            self.assertEqual(secuencia[-1], valor_posicion)
        except ValueError as x:
            self.assertEqual(str(x), "Se debe indicar un número igual o mayor a 0.")

def comprobacion(prueba):
    # Respuesta a pregunta de comprobación
    if prueba == "S":
        # Si la respuesta es S ejecutamos la prueba
        unittest.main()

if __name__ == "__main__":
# Cantidad de números a visualizar
    veces = int(input("Indica cuantos números de Fibonacci deseas calcular: "))
# Se llama a la función de fibonacci indicándole la cantidad recogida
    fibonacci(veces)
# Preguntamos por si se quiere realizar la comprobación de Unitest
    prueba = input("\n¿Deseas realizar la comprobación de Unitest?(S/N): ")
# Y ejecutamos la función que comprueba la respuesta recogida
    comprobacion(prueba)