# Ejercicio 9: mostrar una frase sin espacios y contar su longitud
# hacer un programa donde el usuario ingrese una frase, se le devolverá
# la misma frase sin espacios en blanco, y además un contador de cuántos
# caracteres tiene la frase (sin contar los espacios en blanco)
# ejemplo: frase igual vivir por siempre en paz
# frase final = vivirPorSiempreEnPaz
# N° de caracteres = 20

frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")
