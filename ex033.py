a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))
# Verificando qual é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando qual é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))