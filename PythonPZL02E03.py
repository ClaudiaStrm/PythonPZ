#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve 
#pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
#e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
#Caso contrário mostrar tais variáveis com o conteúdo ZERO.

peso = int(input('Informe a quantidade pescada em quilos: '))
if peso <= 50:
	multa = excesso = 0
	
else:
	excesso = peso - 50
	multa = excesso * 4

print('O excesso é de %dkg e a multa é de R$%d.' %(excesso, multa))