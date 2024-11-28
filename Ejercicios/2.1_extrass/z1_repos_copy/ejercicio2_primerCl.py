peso = -1
precio_por_kilo = -1
tipo = " "
seguir = " "
precio_final_por_entrada =  0
acumulador_precio = 0
descuento_por_kilos = 0
precio_con_descuento = 0
precio_tipo_mas_caro = 0
tipo_mas_caro = " "
acumulador_peso = 0
acumulador_precio_por_kilo = 0
promedio_total = 0

while(True):
    while(True):
        peso = int(input("Ingrese el peso del ingrediente : "))
        if peso >= 10 and peso <= 100:
            break
    while(True):
        precio_por_kilo = int(input("Ingrese el precio por kilo : "))
        if precio_por_kilo > 0 :
            break
    while(True):
        tipo = input("Ingrese el tipo : (v (vegetal) / a (animal) / m (mezcla) )")
        if tipo == "v" or tipo == "a" or tipo == "m":
            break
    if precio_por_kilo>precio_tipo_mas_caro:
        tipo_mas_caro = tipo
    precio_final_por_entrada = precio_por_kilo*peso
    acumulador_precio += precio_final_por_entrada
    seguir = input("Desea seguir ingresando datos? ( si/ no ) ")
    acumulador_peso += peso
    acumulador_precio_por_kilo += precio_por_kilo
    if seguir == "no":
        break
promedio_total = acumulador_precio_por_kilo*acumulador_peso
if acumulador_precio > 100 and acumulador_precio < 300:
    descuento_por_kilos = 0.15
elif acumulador_precio > 300:
    descuento_por_kilos = 0.25
print("El importe total a pagar es ", acumulador_precio ,".")
if descuento_por_kilos > 0:
    precio_con_descuento = acumulador_precio * descuento_por_kilos
    print("El importe con descuento es ", precio_con_descuento ,".")
print("El tipo de alimento más caro es : ", tipo_mas_caro ,".")
print("El promedio de precio por kilo es ", promedio_total ,".")

# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
# preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
# PESO: (entre 10 y 100 kilos)
# PRECIO POR KILO: (mayor a 0 [cero]).
# TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
# El importe total a pagar, BRUTO sin descuento.
# El importe total a pagar con descuento (Solo si corresponde).
# Informar el tipo de alimento más caro.
# El promedio de precio por kilo en total.
