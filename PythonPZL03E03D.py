#3. Verifique se um inteiro positivo n é primo.
num = int(input('Informe o número: '))
div = 2 
while num%div != 0:
	resto = num%div
	div = div + 1

if num == div:
	r = 'é'
else:
	r = 'não é'

print('O número %d %s primo!' %(num, r))
		
	