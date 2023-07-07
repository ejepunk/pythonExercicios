from datetime import date
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    print('Você ainda vai ter que se alistar! Faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar!')
else:
    print('Você não precisa mais se alistar! Já se pasaram {} anos'.format(idade - 18))