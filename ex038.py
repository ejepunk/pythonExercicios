n1 = int(input('Diga um numero!'))
n2 = int(input('Diga outro numero!'))
if n1 > n2:
    print('O {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('O {} é menor que {}'.format(n1, n2))
else:
    print('O {} é igual que {}'.format(n1, n2))
