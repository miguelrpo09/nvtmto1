# 1. Leer el nombre de 10 frutas {nombre, color y precio} para preparar un salpicón; 
# 2. el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido inverso al ingresado+(1)


import os
os.system ("cls")
i=1
frutas=[]
print("*******MENU*******")
print("(1) Crear una fruta")
print("(2) Mostrar listado de frutas")
print("(3) Mostrar las frutas al reves")
print("(0) Terminar")
while(i!=0):
    fruta={}
    i=int(input("Digita una opción: "))
    if(i==1):
        print("Crear la información de una fruta")
        #append
        fruta['nombre']=input("Digita el nombre de la fruta: ")
        fruta['color']=input("Digita el color de la fruta: ")
        fruta['precio']=int(input(f"Digita el precio de la fruta: "))
        frutas.append(fruta)
        print("*******MENU*******")
        print("(1) Crear una fruta")
        print("(2) Mostrar listado de frutas")
        print("(3) Mostrar las frutas al reves")
        print("(0) Terminar")
    elif(i==2):
        print("Mostrar listado de frutas")        
        for elemento in frutas:           
            print(elemento)
            print("")
        print("*******MENU*******")
        print("(1) Crear una fruta")
        print("(2) Mostrar listado de frutas")
        print("(3) Mostrar las frutas al reves")
        print("(0) Terminar")
    elif(i==3):
        print("Mostrar listado de frutas al revez")
        frutas.reverse()      
        for item in frutas:
            print(item)
            print("")
        print("*******MENU*******")
        print("(1) Crear una fruta")
        print("(2) Mostrar listado de frutas")
        print("(3) Mostrar las frutas al reves")
        print("(0) Terminar")        
    elif(i==0):
        break
    else:
        print("Digite una opcion valida.")
else:
    print("Digite una opcion valida.")

   