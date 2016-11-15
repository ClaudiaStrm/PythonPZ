#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

l = int(input('Largura da parede (em metros): '))
h = int(input('Altura da parede (em metros): '))

m2 = l * h

lt = m2 / 3 

if ((lt % 18) == 0):
	qlt = lt / 18

else:
	qlt = int((lt /18) +1)

pr = qlt * 80

print (m2, lt, qlt, pr)

print('São necessárias %d latas e o preço total é R$ %d.' %(qlt, pr))
