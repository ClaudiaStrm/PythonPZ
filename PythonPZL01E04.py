sal = int(input('Informe o valor do salário: '))
aumen = int(input('Informe o valor do aumento em %: '))
pcnt = sal*aumen/100
nsal = sal + aumen
print('O valor do aumento é %.2f' %pcnt)
print('O novo salário é de R$ %.2f' %nsal) 
