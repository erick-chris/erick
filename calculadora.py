# coding: utf-8
"""
Calculadora
Função: operações ariméticas básicas
"""
sair = False
while sair == False:

	print ("Calculadora TOP")

	num1 = input("Digite o primeiro número:")
	num1 = float(num1) 
	operador = input("Digite o operador:")
	num2 = input ("Digite o segundo número:")
	num2 = float(num2)

	if operador == "+":
		operação = num1 + num2

	if operador == "-":
		operação = num1 - num2

	if operador == "*":
		operação = num1 * num2

	if operador == "/":
		operação = num1 / num2

	print("Resultado:")
	print(operação)

	teste = input("Deseja sair? (s/n)")
	if teste == "s":
		sair = True