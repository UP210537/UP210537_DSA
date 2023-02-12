# Lists in advanced applications
#import numpy as np
squares = [x ** 2 for x in range(10) if x**2 % 2 ==0] # Esta es una lista no un vector
# Que operacion voy a hacer    Cuántas veces   Vas a filtrar algo
print(squares)

board = []
# Meter valores por un for
for i in range(8):
    row = ["A" for i in range(8)] #Lo hará 8 veces
    board.append(row) #Los va a adicionar
print(board) #El tablero será 8 por 8

'''
a = np.array([7,2,4]) #Esta lista pasamela a un vector (arreglo) Arreglo
b = np.array([[1, 2, 3, 6],
            [4, 5, 6, 15]
            [7, 8, 9, 24]]) # 3 X 4   Arreglo bidimensional

c = np.array([[[2, 17, 23, 1],[45, 78, 45, 3],[5, 6, 7, 8]],
            [[9, 27, 13, 9], [35, 68, 35, 5], [1, 2, 3, 4]]]) # Arreglo tridimensional

print("c", c.shape) # 2,3,4 #(shape = dame su forma) (Dice filas, columnas y otra dimension más)
print(c[1][2][3]) # Fila, columna, numeros dentro
print("-----------------")

print(b.shape) #(F, C)
print(b.shape[0]) #Trae las filas unicamente) (F -> 0, C -> 1)
print(b[2,1])
print("np.where", np.where(a > 3)) #Trae el indice, no los datos. En donde se encuentran el 7 y el 4 del "a"
print("-----------------")

board1 = [[i+j for j in range(3)] for i in range(7)]
#    que se hará   0..2 (for de adentro)    0..6 (for padre)        7 X 3
board2 = np.array(board1) #Esa lista la está pasando a arreglo
print("F, C", board2.shape)
print("Len ", len(board2)) #El len seguirá dando las filas (no la multiplicación)
print(board2) ; print()  #Muestro el tablero 2
print("-----------------")


print("Days") #Va uno por uno // Queda a manera de renglon
for day in board1:
    print(day)
print()

for day in board2: # Va uno por uno // Especificamente a cada elemento
    for item in day:
        print(item, end ="\t")
    print()
print()
'''

#3 edificios, 15 pisos, 20 cuartos en cada piso
#True = Ocupado
#¿Cuántos cuartos estan desocupados?
rooms = [[[False for r in range(20)] for f in range(15)]for b in range(3)]
