import unittest

# Ejecución python -m unittest

# Función fibonacci

def fibonacci(veces):
    x = 0
    num1 = 0
    num2 = 1
    while (x <= veces):
        x = x + 1 
        num1 = num2
        num2 = num1 + num2
        print(x)


fibonacci(10)