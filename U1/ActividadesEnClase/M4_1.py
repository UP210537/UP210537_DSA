#import numpy as np

def ispar(x): # Quiero que regrese un boliano
    if x % 2 == 0:
        return True
    else:
        return False
print(ispar(50))

y=(lambda x:x+3)(4)  # al poner lambda se convierte en funcion y a esa funcion, le introducimos ese valor (el 4)
print(y)

lista = [4,7,1]
ordenada = sorted(lista) # Ordena la lista
print(ordenada)

y = list(map(lambda x:x+3,lista)) # Le aplica la funcion lambda a cada valor que tiene la lista, y la convierte tambien en lista
# Map = reestructuralo y dejalo al final como una lista.
print(y)

mayores = list(filter(lambda x: x>2, lista)) #De cada valor de lambda dime, los mayores a dos. De esos filtralos y dejalos a manera de lista.
print("Mayores: ", mayores)

# Operador ternario

a = 10
b = 0
c = a/b if b!=0 else -1
print(c)

