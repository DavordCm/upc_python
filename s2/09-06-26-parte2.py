#Entrada variable
aLtura:float=0.0
aNcho:float=0.0
Largo:float=0.0
costoToTal:float=0.0

#Entrada del algoritmo

aLtura=float(input("INGRESAR ALTURA; "))
aNcho=float(input("INGRESAR ANCHO; "))
Largo=float(input("INGRESAR L; "))
costoToTal=float(input("INGRESAR costo; "))

#Algortimo
importarTotal = (aLtura*aNcho*Largo)*costoToTal

#Salida de dato
print("==================================")
print(f"La importación total es de: {aLtura:.2f}, {aNcho:.2f}, {Largo:.2f}, {costoToTal:.2f}")
#print("La importacion total es de: " ,aLtura,aNcho,Largo,costoToTal)"
print("==================================")
print("s/",importarTotal)
print("==================================")
