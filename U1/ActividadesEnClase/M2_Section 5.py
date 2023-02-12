def doble(x):
    y = x*2
    return y
    
#Cómo hacer una función?
def ordenear(stock): #Def = definir una funcion def -> los parametros -> las variables -> dos puntos
    return len(stock) == 0 

#Cómo se hace un vector?
a = [5,2,7,9,3]

#For con el vector
for i in range(0, len(a)): #Sacando la longitud. LO hará de 0..5 {realmente es un 4   ->   [0..5)}
    print("FOR: ", a[i])

# bubble
for i in range(0, len(a)+1 - i-2):
    for j in range(0,len(a)+1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x
print(a)

#Sintáxis del if
b = 10
if b > 20:
    print("Mayor a 10")
else:
    print("Menos a 10")
print(doble(10))

print("...Hecho")