Boletos = 1000
T = 0

print ("Cuanto dinero tienes? ")
D = int(input())

for i in range (1, Boletos+1):
    while D >= i:
        D = D - i
        T+=1
        break

print ("Alcanzaste", T  , "boletos c:")
print ("Tu cambio fue de", D)