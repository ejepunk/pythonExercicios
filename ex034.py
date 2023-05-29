sa = float(input('Quanto vc recebe atualmente?'))
if sa <= 1250:
    al = (1250 * 0.15)
    sn = (1250 * 0.15) + 1250
else:
    al = (1250 * 0.1)
    sn = (1250 * 0.1) + 1250
print('Vc recebera a partir de agora um aumento de R${:.2f} e seu salario ficar R${:.2f}'.format(al, sn))