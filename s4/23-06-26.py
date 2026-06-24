#edad con if

#edad : int

#edad = int(input("Ingrese su edad: "))

#if edad >= 0:
#    print("valido")
#else:
#    print("no valido")

#///////////////////////////////////////////////////////////////

#Operacion logico

edad : int
resultado: str
edadM: int = 120

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <=  edadM :
    resultado="valido"
else:
    resultado="no valido"
print(resultado)