import os

os.system("cls")

try:
    archivo=open(r"C:\Users\Asael Tapia\Documents\PARADIGMAS\hola.txt")
    data=archivo.read()
    print(data)
except IOError:
    print("Error al leer el archivo")
finally:
    archivo.close()