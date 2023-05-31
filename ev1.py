cantidad_niños = 0
cantidad_jovenes = 0
cantidad_adultos = 0

monto_total = 0

print("BIENVENIDO A CINE MORO")
print("========================================")
print("             PRECIOS")
print("========================================")
print("Niño (1-13 años)          Precio $5500")
print("Joven (14-21 años)        Precio $7000")
print("Adulto (Mayor de 22 años) Precio $9000")
print("========================================")

while True:
    print()
    categoria = input("Ingrese la categoría de la entrada (Niño, Joven, Adulto): ")
    
    if categoria == "Niño":
        tarifa = 5500
    elif categoria == "Joven":
        tarifa = 7000
    elif categoria == "Adulto":
        tarifa = 9000
    else:
        print("Categoría inválida. Por favor, ingrese una categoría válida.")
        continue
    
    print("----------------------------------------")
    
    while True:
        cantidad_entradas = input("Ingrese la cantidad de entradas: ")
        
        try:
            cantidad_entradas = int(cantidad_entradas)
            if cantidad_entradas <= 0:
                print("Cantidad inválida. Por favor, ingrese un número mayor a cero.")
            else:
                break
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número válido.")
    
    print("----------------------------------------")
    
    if categoria == "Niño":
        cantidad_niños += cantidad_entradas
    elif categoria == "Joven":
        cantidad_jovenes += cantidad_entradas
    elif categoria == "Adulto":
        cantidad_adultos += cantidad_entradas
    
    monto_pagar = tarifa * cantidad_entradas
    
    print("Total a pagar: $" + str(monto_pagar))
    
    monto_total += monto_pagar
    
    continuar = input("¿Desea registrar otra venta? (s/n): ")
    
    if continuar.lower() != "s":
        break

total_entradas = cantidad_niños + cantidad_jovenes + cantidad_adultos

porcentaje_niños = (cantidad_niños / total_entradas) * 100
porcentaje_jovenes = (cantidad_jovenes / total_entradas) * 100
porcentaje_adultos = (cantidad_adultos / total_entradas) * 100

print("========================================")
print("Total a pagar: $" + str(monto_total))
print("========================================")
print("Cantidad de entradas vendidas por categoría:")
print("Niños: " + str(cantidad_niños) + " (" + str(porcentaje_niños) + "%)")
print("Jóvenes: " + str(cantidad_jovenes) + " (" + str(porcentaje_jovenes) + "%)")
print("Adultos: " + str(cantidad_adultos) + " (" + str(porcentaje_adultos) + "%)")
print("========================================")
print("Gracias por su compra, disfrute la función.")

