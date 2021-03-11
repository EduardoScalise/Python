v1 = input('Digite um número: ')
print(v1, type(v1))

v2 = float(input('Digite um valor: '))
print(v2, type(v2))

v3 = str(input('Digite algo: '))
print(v3, type(v3))

v4 = bool(input('novamente!: '))
print(v4, type(v4))

v5 = input ('Testar se é numero: ')
print(v5, v5.isnumeric())

v6 = input ('Testar se é alfabetico: ')
print(v6, v6.isalpha())

v7 = input('Testar AlphaNumerico: ')
print(v7, v7.isalnum())