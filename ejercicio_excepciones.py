import os

os.system("cls")


def registrar_estudiantes():
    try:
        nombre = input("Introduce el nombre del alumno: ")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        numero_de_cuenta = int(input("Introduce el número de cuenta: "))
        if numero_de_cuenta < 0:
            raise ValueError("El número de cuenta no puede ser negativo.")

        edad = int(input("Introduce la edad del alumno: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")

        calificacion = float(input("Introduce la calificación del alumno: "))
        if calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 0 y 10.")

        # Si todo es válido, se muestra la información del estudiante
        print(f"Estudiante registrado: {nombre}, Número de cuenta: {numero_de_cuenta}, Edad: {edad}, Calificación: {calificacion}")

    except ValueError as e:
        print(f"Error: {e}")

registrar_estudiantes()


        
