# en esta clase veremos la sentencia If Else
'''condicion = 10
if condicion ==True:
    print(" condicion Verdadera")
elif condicion == False:
    print("condicion Falsa")
else:
    print(" Condicion sin especificar")
'''
# Conversion de nuemro a texto

'''num = int(input(" Digite un numero en el rango del 1 al 3 :"))
numtexto = ""
if num == 1:
    numtexto = " Numero uno"
elif num == 2:
    numtexto = " Numero dos"
elif num == 3:
    numtexto = " Numero tres"
else:
    numtexto = " Has ingresado un numero fuera del rango "
print(f"El numero ingresado es : {num} - ({numtexto})")
'''

condicion = False
# if condicion:
#     print("condicion verdadera")
# else:
#     print("condicion falsa")

print(" condicion verdadera") if condicion else print(" condicion Falsa")