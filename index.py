num1 = int(input("ingresa el primer numero:"))

print("El primer numero es :" , num1)
num2 = int(input("ingresa el segundo numero:"))

print("El segundo numero es :" , num2)

operacion= str(input("¿Que deseas hacer?"+"\n suma \n resta \n multiplicacion \n divicion "))




if operacion == "suma":
	print("Tu respuesta es :" ,num1 + num2)

if operacion == "resta":
	print("Tu respuesta es :" ,num1 - num2)

if operacion == "multiplicacion":
	print("Tu respuesta es :" ,num1 * num2)

if operacion == "divicion":
	print("Tu respuesta es :" ,num1 / num2)

else:
	print("la calculadora se a apagado")
