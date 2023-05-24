#EJEMPLO DE USO DE GITHUB
print ("INGRESO DE DATOS: ")
print ("------------------")
vnom=input("Ingrese su nombre: ")
while True:
 try:
     vedad=int(input("Ingrese su edad: "))
     break
 except:
    print("Error de ingreso")
print ("------------------")
print (f"Su nombre es: {vnom}")
print (f"Su edad es: {vedad}")
print ("PROGRAMA FINALIZADO")