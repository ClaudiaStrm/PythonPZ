cigdias = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Há quantos anos você fuma?'))
totdias = anos*365
totcig = totdias*cigdias
diasp=totcig/144
print('Você perdeu no total %.1f dias' %diasp)  
