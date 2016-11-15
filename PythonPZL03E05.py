#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles 
#usando o algoritmo de Euclides. 

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a>b :
	dividendo = a
	divisor = b
else:
	dividendo = b
	divisor = a

while dividendo%divisor != 0:
	quociente = dividendo%divisor
	dividendo = divisor
	divisor = quociente
	print(quociente)

print('O MDC entre %d e %d é %d.' %(a, b, quociente)) 