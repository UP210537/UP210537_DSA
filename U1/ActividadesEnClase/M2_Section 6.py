import os
import time

print("What is your last name: ")
lastName = input()

Name = input("What is your name: ")

Edad = int(input("Give me a number: ")) # casting: int()  , float()    Aclara que es entero
print(type(Edad)) # Tipo  Type = te dice que tipo de dato estás manejando. Te das cuenta de que tipo es "int", etc..

complete_name = Name + " " + lastName #Concatenation
print("Hi", complete_name, "your number is: ", Edad)
print("Hola"*2, 2*"Adios")

#os.system("cls")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
