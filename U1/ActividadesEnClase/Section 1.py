# Section 1
print("Hola\nMundo "); print("python")
print("\\")
print("Hola", "Mundo", end="...") # final de linea -> default end="\n"     separacion -> sep=" "
print("Hola", "Mundo", end="\n", sep="-")
print('Cruel '*2)

print('Greg\'s book.')
print("Greg's book")
print('Hola "Mundo" ')

print("'Greg's book.'")
print('"Greg\'s book."')

c= " Jesus"
b= " Maria"
print( b + c)

import array as arr 
a= arr.array('i', [5,2,3])
print(a)
print(a[1])
b=[55,22,"33"] 
print(b[2])
b.append("44") # Agrega cualquier tipo de caracter al vector 
print(b)
b.pop() # Elimina cualquier elemento del vector (No poner nada entre () elimina el ultimo elemento)
print(b)


'''
print('"Greg's book."') Error
'''
