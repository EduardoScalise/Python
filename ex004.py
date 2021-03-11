# Faça um algoritmo que leia o preço e mostre seu novo preço com 5% de desconto

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O valor de {:.2f} com 5% de desconto é: R$ {:.2f}'.format(preco, novo))

# Proximo algoritmo - Reajuste de salario
print('\n','='*60,'\n')
salario = float(input('Qual o salário do funcionário: '))
novosal = salario + (salario * 15 / 100)
print('O atual salrio de R$ {:.2f} com reajuste de 15% fica em R$ {:.2f}'.format(salario, novosal))

# Algoritmo conversao de temperatura. De graus Celsius para Fahrenheit
print('\n','='*60,'\n')
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5 ) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

# Algoritmo para calcular o aluguel do carro
# Pergunte a KM + dias alugados
# Calcule o preço a pagar, sabendo que custa R$ 60 por dia e R$ 0,15 por Km rodado
print('\n','='*60,'\n')
dias = int(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos KM rodou com o carro: '))
print('Ficou {} dias com o carro alugado e percorreu {}KM.\nTotal a pagar: R$ {:.2f}'.format(dias, km, ( (dias * 60) + (km * 0.15) )))