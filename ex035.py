print('informe 3 valores de seguimento para construir um triangulo:')
r1 = float(input('1º valor: '))
r2 = float(input('2º valor: '))
r3 = float(input('3º valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimento formam um triangulo!')
else:
    print('Os seguimento NÃO formam um triangulo!')

