
import os

os.system("cls")
try:
    x=int(input("Introduce un numero: "))
except ValueError:
    print("Introduce un valor valido.")

else:
    print(f"El numero es {x}")