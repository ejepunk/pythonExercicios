dis = float(input('Quantos Km de distancia esta o seu destinho? '))
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
print('Sua passagem custara R${:.2f}'.format(preco))