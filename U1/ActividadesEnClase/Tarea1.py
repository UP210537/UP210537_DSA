#Ecuación
#Solucion


'''
Ejercicio 2:
    Horas            = 12         |  23   |  0   |
    Minutos          = 17         |  58   |  1   |
    (Min) duración   = 59         |  642  | 2939 |
    Finaliza         = 13:16      | 10:40 |  ?   |
Parte entera = //
Con decimales = /
'''

horas = 0
minutos = 1
duracion = 2939

minutosIniciales = minutos + duracion
horasAdicionales = minutosIniciales//60  
minutosTotales = minutosIniciales%60
print("Finalizó a las", horasAdicionales,":",minutosTotales)

