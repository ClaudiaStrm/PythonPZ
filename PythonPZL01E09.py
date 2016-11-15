kmp = int(input('Informe a quantidade de quilômetros percorridos: '))
dias = int(input('Informe a quantidade de dias com o carro: '))
dtotal = 60*dias 
kmt = kmp*0.15
vltotal = kmt+dtotal
print('Valor total a pagar: R$ %.2f.' %vltotal) 
