#Dizemos que um número natural é triangular se ele é produto de três números naturais
#consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro 
#não-negativo n, verificar se n é triangular.
num = int(input('Informe o número: '))
a, b, c, tr = 1, 2, 3, 0
tr = a * b * c

while tr < num:
	tr = a * b * c
	a = a + 1
	b = b + 1
	c = c + 1
	
if tr == num:
	print('O número é triangular!')
else:
	print('O número não é triangular!')