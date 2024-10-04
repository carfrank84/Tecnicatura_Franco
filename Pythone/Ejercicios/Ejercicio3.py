mes = int(input(" Ingrese un mes del año para saber su estacion:"))

if 1 <= mes <= 3:
    print(" La Estacion del año es verano")
elif 4 <= mes <= 6:
    print(" La Estacion del año es Otoño")
elif 7 <= mes <= 9:
    print(" La Estacion del año es Invierno")
elif 10 <= mes <= 12:
    print(" La Estacion del año es Primavera")
else:
    print(f"El mes {mes}""no es valido")
