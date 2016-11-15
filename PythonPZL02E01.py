#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Digite valor do primeiro lado: '))
b = int(input('Digite o valor do segundo lado: '))
c = int(input('Digite o valor do terceiro lado: '))

if ((b - c) < a < (b + c)) & ((a - c) < b < (a + c)) & ((a - b) < c < (a + b)) == True:

	if a==b==c:
		t = 'equilátero' 

	elif a==b or b==c or c==b:
		t = 'isósceles'

	else:
		t = 'escaleno'

	print("Os valores informados formam um triângulo %s!" %t)

else: 
	print ('Os valores informados não formam um triângulo!')