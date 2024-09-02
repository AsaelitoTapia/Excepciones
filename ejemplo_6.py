import os

os.system("cls")

class Mi_exepcion(Exception):
    pass
raise Mi_exepcion("Este en un mensaje de error personalizado.")