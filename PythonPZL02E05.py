#5. Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if ((a>b) & (a>c)):
	maior = a
elif  b > c:
	maior = b
else:
	maior = c

print ('O número maior é o %d.' %maior)

if ((a<b) & (a<c)):	menor = a

elif b < c:
	menor = b
else:
	menor = c

print ('O número menor é o %d.' %menor)


