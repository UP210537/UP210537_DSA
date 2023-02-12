palabra = input("Detector de palindromos c:\nDame una palabra u oración: ")
palabra = palabra.upper() #Los hace mayúsculas
palabra_nueva = ""
for letter in palabra:                            
    if letter not in (" "):    
        palabra_nueva += letter   

if(palabra_nueva==palabra_nueva[::-1]):  
      print("Es un palindromo c:")  
else:  
      print("No es un palindromo :c") 
