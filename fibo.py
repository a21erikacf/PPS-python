import unittest

# Ejecución python -m unittest

# Función fibonacci

def fibonacci(veces):

    contador = 0
    num1 = 0
    num2 = 1
    
    while (contador <= veces):

        numresultado = num1
        num1 = num2
        num2 = num1 + numresultado
        
        contador += 1

        print(num1)

fibonacci(10)