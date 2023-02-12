from random import randrange

print("Numero Secreto - Del 1 al 500")
b = True
d = 0
a = randrange(1, 500)

while b == True: 
    c = int(input("Dime el numero secreto: "))
    if c == a:
        b = False
        print("Felicidades... Lo hiciste en", d, "Intentos")
    elif c > a:
        print("Abajo")
        d+=1
    elif c < a:
        print("Arriba")
        d+=1