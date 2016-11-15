#4. Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a > b and a > c:
	maior = a

elif b > c:
	maior = b

else:
	maior = c

print ('O número maior é o %d.' %maior)