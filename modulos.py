# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def funcion1():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellidos: ").strip().upper()
    print(f"El nombre del alumno es {nombre}  {apellidos}")

def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre del alumno es {nombre}  {apellidos}")

def funcion2():
    nombre = input("Nombre: ").strip().upper()
    apellidos = input("Apellidos: ").strip().upper()
    
    return nombre,apellidos
nom,ape=funcion2()

def funcion4(nom, ape):
    nombre = nom
    apellidos = ape
    
    return nombre,apellidos
nom,ape=funcion4("juan", "lopez")
print(f"El nombre del alumno es {nom}  {ape}")

def borrarPantalla():
    print("\033c")