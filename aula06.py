print('='*15, 'Welcome to Python!', '='*15)
nome = input('Qual seu nome: ')

n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
n3 = float(input('Digite terceira nota: '))
n4 = float(input('Digite quarta nota: '))

print(' Olá {}\n A média da soma das notas é {:.1f}'.format(nome, ( (n1 + n2 + n3 + n4)/4 )))
