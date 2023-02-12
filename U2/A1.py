'''
    - Tarea 1: Biseccion
    - Tarea 2: Numero secreto
        Libreria como se generan nuemeros ramdoms
        Van campurando el numero.
            Te doy 500 y que te diga "Subele", "Bajale" o "Bingo" junto con el conteo
    - Tarea 3: Sumatoria
        Sumatoria
        N = 5
        suma = 1+2+3+4+5 = 15

        Si la suma = 16
        ¿Cuantos boletos ajusto?
        N = 5
            Suma    = 1000     n = 44
                    = 2        n = 1
                    = 6        n = 3
                    = 7        n = 3
    - Tarea 4: Matriz sin repetir
    - Tarea 5: Bubble
    - Tarea 6: Palindromos
'''


infix = '5*(6+2)-12/4'
posfix = '5 6 2 + * 12 4 / -'
P = posfix.split()
P = ['5','6','2','12','4']
def Prioridad (c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c in ['^']:
        return 3
    elif c in ['(']:
        return 4



# Que regrese la prioriodad que tiene
'''
1) + -
2) * /
3) ^
4) ()
'''