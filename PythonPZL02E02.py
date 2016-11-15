#Determine se um ano é bissexto. Verifique no Google como fazer isso...

ano = int(input('Digite o ano: '))

if ano%4==0:
	if (ano%100==0) & (ano%400!=0):
		print("O ano não é bissexto!")
	else:
		print('O ano é bissexto!')
else:
	print("O ano não é bissexto!")
