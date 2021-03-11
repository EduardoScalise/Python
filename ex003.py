# Exercicio: Pintar parede
# Para cada 2m (quadrado) precisa de 1 Litro de tinta

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} X {} e sua área é de {:.2f}m².'.format(larg, alt, area))

tinta = area / 2
print('Para pintar essa parede, vai precisar de {:.2f}l de tinta'.format(tinta))