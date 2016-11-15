#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

dhora = float(input('Quanto você ganha por hora? '))
hmes = int(input('Quantas horas você trabalha por mês? '))

sbruto = dhora * hmes

IR = sbruto * 11/100
INSS = sbruto * 8/100
sind = sbruto * 5/100

sliq = sbruto - IR - INSS - sind

print('Seu salário bruto é R$ %.2f e o líquido é R$ %.2f. \nTotal de descontos em R$: \nIR = %.2f \nINSS: %.2f \nSindicato: %.2f' %(sbruto, sliq, IR, INSS, sind))