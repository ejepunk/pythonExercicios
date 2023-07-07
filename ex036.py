casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto você recebe por mês? '))
tempo = float(input('Em quanto tempo pretende pagar?'))
if casa / tempo >= salario * 0.3:
    print('Infelizmente seu emprestimo foi negado!')
else:
    print('pagando R${:.2f} '.format(casa / tempo))
    print('Emprestimo aprovado!')