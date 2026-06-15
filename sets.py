"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")
set1={"Python", "SQL", "Estructurado"}
print(set1)
for i in set1:
    print(i)
set2={"Hola", True,33,3.1416}
print(set2)
set2_respaldo=set2.copy()
set2.clear
print(set2_respaldo)
print(set2)
set3={""}
print(set3)
set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)
set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)
lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print(lista)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados.
#Solucion 1
print("\033c")
lista_email=[]
set_email={""}
emails=""
opc="si"
while opc == "si":
  lista_email.append(input("Ingresa un email: ").lower().strip())
  set_email.add(input("Ingresa un email: ").lower().strip())
  emails=input("Ingresa un email: ").lower().strip()
  opc=input("¿Deseas ingresar otro? (si/no) ").lower().strip()
set_email=set(lista_email)
lista_email=list(set_email)
print(lista_email)
print(set_email)
print(emails)
#Solucion 2
lista_email=[]
opc=True
while opc:
  lista_email.insert(0, input("Ingresa un email: ").strip())

  opc=input("¿Deseas ingresar otro? (si/no) ").lower().strip()
  if opc == "no":
    opc=False
set_email=set(lista_email)
lista_email=list(set_email)
print(lista_email)

