'''
comments
import mypkg.sibling #(my package)
from mypkg import sibling
'''
# hash (gato)

# PEP 8 -- Style Guide for Python Code
# https://peps.pyhton.org/pep-0008/

# varibales = containers = boxes
# Python is a dinamically-typed 

_n = 1
n = 2
N = 3
_1 = 10
exchange_rate = None

m = 5
m = "Hello"

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'beak', 'class', 
            'continue', 'def', 'elif', 'else', 'except', 'finally', 'for',
            'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlock'] # palabras reservadas (Faltaaan)

# keywords.append() # sirve para pilas pero no para listas, se agrega al final
keywords.insert(2, "Hola") # Posicion y lo que quiero meter
print(keywords)
print("Conteo: ", keywords.count("True")) # Buscará cuantas veces se repite
print("-----------")
print(keywords[1], keywords.index('True')) 
'''
    Imprime None (vectores empiezan en la posicion 0)   
    .index = cual es la posicion de esa palabra
    Si se pone -1, regresa el último de la lista, va para atrás
'''
print(keywords.pop(), keywords.pop(), keywords.pop(1), keywords[1])
'''
    .pop = Muestra (por si quieres guardarlo en una variable). Elimina el último y aparte de que te lo quita, guarda el dato.
    Al meterle índice ya no solo funciona como pila, sino como lista
   
    keywords.pop(1) = Muestra y quita el elemento
    keywords[1] = Solo lo muestra
'''

