nem = int(input('Digite um numero inteiro?'))
print('''escola uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('sua opção: '))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('{} é invalido'.format(opc))