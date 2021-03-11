# Fatiamento de memória
frase = 'Welcome to Python!'
frase2 = 'learning python programming'
frase3 = '    Data Science with Python!     '
print(frase)
print(frase[:7])
print(frase[8:10])
print(frase[11:])
print(len(frase))
print(frase.count('o'))
print(frase.find('Py'))
print(frase.find('Android'))
print('Welcome' in frase)
print('Android' in frase)
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase2)
print(frase2.capitalize())  # Deixa apenas a primeira letra da primeira palavra em maiuscula
print(frase2.title())  # Deixa todos as primeiras letras das palavras em maiusculas
print(frase3)
print(frase3.strip()) # Tira os espaços do início e do fim
print(frase3.rstrip()) # Tira os espaços do lado direito
print(frase3.lstrip()) # Tira os espaços do lado esquero (inicio da frase/variável)
print(frase2.split())
print(frase3.split())