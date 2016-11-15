#Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
#algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado 
#desprezando os centavos. Suponha que as notas para troco sejam as de 
#50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.

conta = int(input('Valor da conta: '))
pag = int(input('Valor do pagamento: '))
pag = pag - conta
n50, n20, n10, n5, n2, n1 = 0, 0, 0, 0, 0, 0

while pag >= 50:
	n50 = n50 + 1
	pag = pag - 50
	print (pag, n50)

while pag >= 20:
	n20 = n20 + 1
	pag = pag - 20
	print (pag, n20)


while pag >= 10:
	n10 = n10 + 1
	pag = pag - 10
	print (pag)

while pag >= 5:
	n5 = n5 + 1
	pag = pag - 5
	print (pag)

while pag >= 2:
	n2 = n2 + 1
	pag = pag - 2
	print (pag)

while pag >= 1:
	n1 = 1 + 1
	pag = pag - 1
	print (pag)

print('O total de notas é', (n50+n20+n10+n5+n2+n1), ', sendo: \n%d de 50, \n%d de 20, \n%d de 10, \n%d de 5, \n%d de 2 e \n%d de 1.' %(n50, n20, n10, n5, n2, n1))
