n = int(input('Digite um numero: '))
res = n % 2
if res == 1:
    print('O numero {} é impar.'.format(n))
else:
    print('O numero {} é par.'.format(n))