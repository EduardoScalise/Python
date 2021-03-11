from math import sqrt
msg = 'Welcome to Python Programming!'
nome = input('Olá, qual seu nome? ')
print(nome, msg)
print('Nice to see you, {}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outor valor: '))
s = n1 + n2
# Abaixo a raiz quadrada do valor do resultado da soma
# raiz = s ** 0.5
raiz = sqrt(s)
print('A soma de {} e {} é {} e a raiz quadrada da soma é {}'.format(n1, n2, s, raiz))
print(' =>'*10,)