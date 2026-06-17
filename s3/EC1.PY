# PSEUDOCODIGO
# cmensual, horasP, factor_rendimiento
# energiaDia, potencia_necesaria, capBaterias

#paneles_calculados
#numero_paneles
#cmensual
#horasP

#factor_rendimiento

#energiaDia < cmensual / 30

#potencia_necesaria < (energiaDia / horasP) / factor_rendimiento

#paneles_calculados < potencia_necesaria / 0.55

#num_paneles < (paneles_calculados)

#ENTRADA
#VARIABLEs
cmensual : float = 0.0
horasP : float = 0.0
factor_rendimiento : float = 0.0
energiaDia : float = 0.0
potencia_necesaria : float = 0.0
cap_Baterias : float = 0.0
paneles_calculados : float = 0.0

num_paneles : int = 0

cmensual = float(input("Ingrese consumo mensual promedio del hogar en kWh: "))

horasP = float(input("Ingrese horas pico de sol al dia: "))

factor_rendimiento = float(input("Ingrese factor de rendimiento del panel: "))

#PROCESO
energiaDia = cmensual / 30
potencia_necesaria = (energiaDia / horasP) / factor_rendimiento
paneles_calculados = potencia_necesaria / 0.55
num_paneles = int(paneles_calculados)

if num_paneles < paneles_calculados:
    num_paneles = num_paneles + 1

cap_baterias = energiaDia / 0.9

#SALIDA
print(
    f"Potencia sistema: {potencia_necesaria:.1f} kW | "
    f"Paneles: {num_paneles} | "
    f"Baterias: {cap_baterias:.2f} kWh")