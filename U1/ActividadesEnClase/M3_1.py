# id-elif-else

#Leap year or Common year
'''
Si no es divisible entre 4 -> Año comun
    sino
        Si no es divisible por 100 -> Año bisiesto
Si no es divisible por 400 -> Año comun

Y si ninguna de esas se cumple, es un año bisiesto

Tip: use the != and % operators.
'''
year = int(input ("Enter a year: "))

if (year%4) != 0:
    print("Año comun")
elif (year%100) != 0:
    print("Año bisiesto")
elif (year%400) != 0:
    print("Año comun")
else:
    print("Año bisiesto")
print("---------------------------")
'''
Ciclo infinito
while True:
    print("Hello")

Mientras una variable sea diferente a 0 (sin importar si es positiva o negativa), entonces tiene un valor
    Por lo que es True hasta que ese sea igual a 0
'''

for i in range(10): # 0..9 range(1,11) = 1..10
    pass        #Pasale
    #continue
    print(i)
    # break
print("Fin")
print("---------------------------")

# Example: word without vowels
user_word = input("Gime a word: ")
user_word = user_word.upper()
new_word = ""
for letter in user_word:                            #Irá trayendo de una por una de las palabras a letter
    if letter not in ("A", "E", "I", "O", "U"):     # Si letter es diferente a una vocal
        new_word += letter                          #Concatenala
print(new_word)
print("---------------------------")

for i in range(3):
    print(i)
else:
    print("else:", i)
print("---------------------------")

for i in range(3):
    print(i)
print("sino:", i)
print("---------------------------")

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("else:", i)
print("---------------------------")

c = 16
'''
2. Si es par su nuevo valor será igual a c/2
3. Si es impar su nuevo valor será igual a 3*c+1
4. Si es desigual a 0, se regresa al punto 2
'''
numbers = [10, 5, 7, 3, 8]
ordenado = sorted(numbers)
print(ordenado)

numbers[0] = 111
print(numbers)

numbers.remove(7)
del numbers[1]
numbers.append
#libreria numpy (para matematicas)


#Metodos 
#Result = data.method(arg)

Name = "Universidad"
r = Name.replace("sida", "Vih") #Remplaza cierta parte de la palabra ("parte que vas a remplazar", "Parte que va a agregar")
print (r)

My_List = [] #En python se puede generar una lista vacia
suma=0
for i in range(5):
    My_List.append((i+1)*10)
    suma+=My_List[i]
print(My_List)
print(suma)
#print(np.sum(My_List))

#swap

a = 5
b = 6
a, b = b, a
print(a, b)

n = 5
a = [10, 20, 30, 40, 50]

print (a)

for i in range (0, n):

    l = -5
    a[i] = a[l+1]
    l = l + i
    print (l)

print (a)

#listas

my_list = [1, 'a', ["list", 64, [11,22],False]]
print(my_list[2][2])
print(my_list[2][2][1])
del my_list

nombre = "Universidad Politecnica"
print(nombre[6:10])
x = nombre.split()
print(x[1])

