def calcular_salario(horas_trabajadas, tarifa_pago):
    salario = horas_trabajadas * tarifa_pago
    return salario
salarios_totales = 0
for i in range(5):
    horas = float(input(f" Ingrese las horas trabajadas para la persona {i+1}:"))
    tarifa =float(input(f" Ingrese las horas trabajadas para la persona {i+1}:"))

    salario_persona = calcular_salario(horas, tarifa)
    salarios_totales += salario_persona
    print(f"El salario de la persona {i+1} es: {salario_persona}")

print(f"\nLa sumatoria de todos los salarios es : {salarios_totales}")

