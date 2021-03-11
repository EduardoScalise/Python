print('='*15,' Welcome to Python Programming ','='*15)
medida = float(input('Digite uma distância em metros: '))
print(' A medida de {}m\n corresponde a {}cm e {}mm'.format(medida, (medida * 100), (medida * 1000) ))

print('='*60,'\n Exercicio de Tabuada\n')
num = int(input('Digite um número para ver sua tabuada: '))
print('{} X {} = {}'.format(num, 1, num*1))

print('='*60, '\n Conversao de moeda\n')
real = float(input('Quanto em reais para converter em Dollar. R$ '))
dolar = real / 5.49
print('Com R$ {:.2f} corresponde a US$ {:.2f}'.format(real, dolar))
