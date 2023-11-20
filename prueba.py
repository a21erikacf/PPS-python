# x = 11
# 
# if x > 5 and x < 10:
#     print("x =",x)
#     print ("x está entre 5 y 10")
# else:
#     if x > 10:
#         print("x =",x)
#         print ("x es mayor que 10")
#     else:
#         print("x =",x)
#         print("x es menor que 5")
# 
# 

# contador = 10
# while contador > 5:
#     print(contador)
#     contador -= 1

#import os

#directorio = os.getcwd()

#print(os.listdir(directorio))

#os.mkdir("carpeta")
#os.rmdir("carpeta")

#archivo = "./carpeta"

#if os.path.exists(archivo):
#    print("El archivo",archivo,"existe")
#else:
#    print("El archivo",archivo,"no existe")


#def promedio():
#    print("Introduce un número (o 'stop' para parar)")
#    numeros = []
#
#    while True:
#        teclado = input()
#        if teclado == "stop":
#            #print(numeros)
#            cantidad = sum(numeros)
#            resultado = cantidad/len(numeros)
#            print(resultado)
#            break
#        else:
#            numeros.append(int(teclado))
#
#promedio()