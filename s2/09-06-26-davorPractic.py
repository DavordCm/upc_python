#tipo 1
#User , num = input("Insertar Usuario: "), int(input("Insertar edad: "))
#tipo2
User = input("Insertar Usuario: ")
num = int(input("Insertar edad: "))


if num > 20:
    print("La edad de ", User, " es de " , num , " Por lo cual es mayor ")

elif num < 13:
    print ("La edad de ", User, " es de ", num , " Por lo cual es menor" )
else:
    print("La edad de", User, "es de", num, "por lo cual está en el rango intermedio")
