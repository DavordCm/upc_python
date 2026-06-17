#Defenir una funcion de coco y melon
#def funcion(coco: int, melon):
#    print("sumas:",coco + melon )
#    print("resta:",coco - melon)
#    print("multipicacion:",coco * melon)
#   print("division:",coco / melon)

#Variables    
#coco = int(input("Insertar dato 1: ")) ; melon = int(input("Insertar dato 2: "))

#funcion(coco, melon)

#PRACTICA DE FUNCIONES
#Edades y nacimientos

nombre = input("Ingrese su nombre: ")
mIedad = int(input("Ingrse su edad: "))

nacimiento = 2026 - mIedad

def edad (nacimiento):
    print("Su nacimiento es: ", nacimiento)
edad(nacimiento)

if nacimiento < 20:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

print ("El joven",nombre,"tiene de edad de", mIedad ,"y su nacimiento es del", nacimiento)