vl = int(input('Informe o valor da mercadoria: '))
dsc = int(input('Informe o valor do desconto em %: '))
vldsc = vl*dsc/100
vltotal = vl - vldsc
print('O valor do desconto é R$ %.2f' %vldsc)
print('O valor total do produto é R$ %.2f' %vltotal) 
