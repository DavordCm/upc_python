# PSEUDOCODIGO
# INICIO
# horas, gramos_filamento, consumoXwatts, tarifa_kwh
# precio_kg_filamento, costo_material
# consumo_kwh, costo_electrico, costo_desgaste, costo_total

#calcular_costo_impresion(horas, gramos_filamento, consumoXwatts, tarifa_kwh)
#     precio_kg_filamento < 25
#     costo_material < (gramos_filamento / 1000) * precio_kg_filamento
#     consumo_kwh < (horas * consumoXwatts) / 1000
#     costo_electrico < consumo_kwh * tarifa_kwh
#     costo_desgaste < horas * 2
#     costo_total < costo_material + costo_electrico + costo_desgaste
#     Retornar costo_total
# costo_material < (gramos_filamento / 1000) * 25
# consumo_kwh < (horas * consumoxwatts) / 1000
# costo_electrico < consumo_kwh * tarifa_kwh
# costo_desgaste < horas * 2
# costo_total < calcular_costo_impresion(horas, gramos_filamento, consumoXwatts, tarifa_kwh)

#INICIO
def calcular_costo_impresion(horas, gramos_filamento, consumoXwatts, tarifa_kwh):
    precio_kg_filamento = 25
    costo_material = (gramos_filamento / 1000) * precio_kg_filamento
    consumo_kwh = (horas * consumoXwatts) / 1000
    costo_electrico = consumo_kwh * tarifa_kwh
    costo_desgaste = horas * 2
    costo_total = costo_material + costo_electrico + costo_desgaste
    return costo_total
#VARIABLES
horas = float(input("Ingrese horas de impresion: "))
gramos_filamento = float(input("Ingrese gramos de filamento consumidos: "))
consumoXwatts = float(input("Ingrese consumo electrico promedio en watts: "))
tarifa_kwh = float(input("Ingrese tarifa electrica por kWh: "))

costo_material = (gramos_filamento / 1000) * 25
consumo_kwh = (horas * consumoXwatts) / 1000
costo_electrico = consumo_kwh * tarifa_kwh
costo_desgaste = horas * 2
costo_total = calcular_costo_impresion(
    horas,
    gramos_filamento,
    consumoXwatts,
    tarifa_kwh
)
#FIN
print(
    f"Material: ${costo_material:.2f} | "
    f"Energia: ${costo_electrico:.2f} | "
    f"Desgaste: ${costo_desgaste:.2f} | "
    f"Total: ${costo_total:.2f}"
)
