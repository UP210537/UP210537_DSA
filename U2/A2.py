'''
Calculadora:
()
* / + -
Funciones: Ln Log sin acos
'''
'''
Posfix a Valor
Prefix a Posfix

infix  = 5+(6+2)-12/4
posfix = 5 6 2 + * 12 4 / -   (Por muchos parentesis q meta, no los maneja aquí)
           ----- 
             8
        ---------- -----
            40       3
            ---------------
                  37
'''
'''
Algorith: Postfix to value
P = Postfix Expression Vector
Value = Result
1. add ")" at the final P as centinela
            P = 5 6 2 + * 12 4 / -)
                    Algoritmo:
                    P = ['5','6','2','+',...'-']
                    P.append(')')
2. Scan P until fins ")"
    3. If is an operand, push to Stack (Stack = Pila) Numero
    4. If is an operator:
        a) B=pop from Stack, A=pop from Stack
        b) C = A operator B
        c) push(C) to Stack
'''
P = [5,6,2,'+','*',12,4,'/','-']
Stack = []
P.append(')')
for i in range(0, len(P)): 
    if type(P[i]) == int:
        B = P.pop() 
        print(B)

