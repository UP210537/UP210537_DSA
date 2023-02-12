def saludo(name):  #Funcion tipo void
    print("Welcome to Python", name)

def potencia(base, exponente=2):  #Funcion default o predefinido 
    return base**exponente

name = input("Name: ")      #Funcion
saludo(name)

y = potencia(2,3)                       # Por posicion
y = potencia(exponente=3, base=2)       # Por nombres
y = potencia(2, exponente=3)            #Por posicion y por nombre
y = potencia(2)                         #Si no se lo das, entonces agarra por default el dos de la linea 4


def cuadratica1(a,b,c):
    return-(b)+((b**2 - 4*a*c)(**.5))/(2*a)   #Checar

y = cuadratica1(1, c=15, b= -8)
print(y) #5


