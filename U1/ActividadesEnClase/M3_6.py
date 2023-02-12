# Operaciones en listas

a = 5
b = a
print(b) # Imprime 5
a = 6
print(b) # Imprime 5

list_1 = [3,5]
list_2 = list_1 #No pasa los valores, pasa la direccion de memoria // Copia el nombre del arreglo, no su contenido

print(list_2)
list_1[0] = 10
print ("--->", list_2) #Como tienen la misma direccion de memoria, se hizo un cambio y al mismo tiempo se lo hizo a la lista 2

list_1 = [3, 5, 8, 2, 9, 7]
#         0  1  2  3  4  5
#                    -2 -1
list_2 = list_1[:] #Ahora está pasando el contenido, no la dirrecion de memoria // : = Un comienzo y un fin. De donde empieza a donde acaba
#Por lo que son variables distintas.
list_1[0] = 10
print(list_2)
print("Lista1 --->")
print(list_1)
print(list_1[2:4])                   # [   :  ) del 8 a 2 (pq de ese lado el limite no lo toca)
print(list_1[:])                     # Si no digo nada, son todos
print(list_1[0: len(list_1)])        # Esta tomando el tamaño de la lista // Es del 0 al 5 (traer todos)
print(list_1[1:-1])                  # [1 : el ultimo pero sin tocarlo]
print(list_1[1:])                    
print(list_1[:3])                    # [0 : 3] sin tocar el 3

del list_1[1:3]
del list_1[:] #Borra el contenido
del list_1    #Borra la variable

my_list = [10, 3, 12, 8, 2]
print(12 in my_list) #El 12 está en la lista? Regresa true o false

largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
#print(np.max(my_list))