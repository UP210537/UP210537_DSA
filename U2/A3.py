'''
Algoritmo de infix a postfix
1. Poner "(" empezando la expresión Q y ")" al final de la misma 
2. Escanear Q de izq a derecha y repetir paso 3 al 6 por cada elemento de Q (Ciclo)
3. Si es un operando adicionarlo a P (operando = numerito)
4. Si es un "(" hacer un push a STACK
5. Si es un operador:  
    Haz un pop repetidamente en el STACK y añadirlo a P mientras tenga la misma o más alta prioridad de preferencia que el operador.
    Añade el operador al STACK
    (si es menor o igual, sacas el ultimo y pones el q tienes)
    (si es mayor, solo lo añades)
6. Si es ")"
    Hacer un pop repetdiamente en el stack hasta que se encuentre un "("
    pop al STACK el último parentesis y no se añade a P

Ejemplo:
    Q = (5*(6+2)-12/4)
    P = 5 6 2 + * 12 4 / - (resultado)

    Q = 1/(x +1/(x+1/(x+1/x)))
        (1/(x +1/(x+1/(x+1/x)))) 
    P = 1 x 1 x 1 x 1 x / + / + / + /             
'''
