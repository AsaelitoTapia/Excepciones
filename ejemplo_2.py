

try:
    x=int(input("Introduce un numero: "))
    y=10/x
except ValueError:
    print("Debes de introducir un numero valido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")