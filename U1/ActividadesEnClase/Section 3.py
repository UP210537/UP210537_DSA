#Operators - data         manipulation tools

entero = 7 // 2   #  -7//2  rounding goes toward the lesser integer value (floor division) 
'''
Floor y Ceil:
floor(5.1) será igual a 5
ceil(5.1) será igual a 6
    Negativos:
    floor(-5.1) será igual a -6
'''
residuo = 7 % 2  # Modulo
potencia = 2**3
raiz = 16 ** .5
#when both ** arguments are integers, the result is an entero
#when at least one ** argument is a float, the result float

print(entero)
print(residuo)
print(potencia)
print(-2 ** 2)

print(12 % 4.5)        # 3.0
# 12    //  4.5   gives  2.0
# 2.0   *   4.5   gives  9.0,
# 12    -   9.0   gives  3.0,

print(-4 - -4)      #unary operator (unario = signo de un numero)
print(9 % 6 % 2)    #left-sided binding
print(2 ** 2 ** 3)  #right-sided binding

