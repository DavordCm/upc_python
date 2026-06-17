#Entrada de datos
Htrabajo:float=0.0
Pago_Hora:float=0.0

Importe_Sueldo_Final:float=0.0

#
Htrabajo = float(input("INGRESAR HORA: "))
Pago_Hora = float(input("INGRESAR PAGO POR HORA: "))
Des:float=0.1

#Algoritmo
Importe_Sueldo_Final = (1 - Des)*Htrabajo*Pago_Hora

#Salida de datos
print("#################")
print("Descuento:",Des,"%")
print("El importe final es ", "S/",Importe_Sueldo_Final)
print("#################")
