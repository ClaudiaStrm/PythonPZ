#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.

n = int(input('Insira um número de 1 a 10: '))

while ((n<0) | (n>10)):
	print('Número inválido!')
	n = int(input('Insira um número de 1 a 10:'))

print('Número válido!')