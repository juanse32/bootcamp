#-----variables---------------------#


num1 = int(input("ingresa el primer numero: "))

print("El primer numero es :" , num1)
num2 = int(input("ingresa el segundo numero: "	))

print("El segundo numero es :" , num2)
contador = True

operacion= int(input("""¿ingresa el numero de la operacion que deseas hacer?""))
			\n 1 suma 
			\n 2 resta 
			\n 3 multiplicacion
 			\n 4 divicion 
			\n 5 apagar calculadora \n 
			numero :"""))




#-----condiciones---------------------#

while contador ==True:
	if operacion == 1:
		print("Tu respuesta es :" ,num1 + num2 ," \n ")
		

	elif operacion == 2:
		print("Tu respuesta es :" ,num1 - num2," \n ")

	elif operacion == 3:
		print("Tu respuesta es :" ,num1 * num2," \n ")

	elif operacion == 4:
		print("Tu respuesta es :" ,num1 / num2," \n ")

	elif operacion == 5:
		print("la calculadora se a apagado"," \n ")
		contador= False
		break
	
	else:
		print("ou ese numero no esta disponible  intentemolos de nuevo")



	print("intentemolos de nuevo")
	
	num1 = int(input("ingresa el primer numero:"))
	num2 = int(input("ingresa el segundo numero:"))
	operacion= int(input("""¿ingresa el numero de la operacion que deseas hacer?""
			\n 1 suma 
			\n 2 resta 
			\n 3 multiplicacion
 			\n 4 divicion 
			\n 5 apagar calculadora \n 
			numero :"""))



print("el programa a finalizado")
