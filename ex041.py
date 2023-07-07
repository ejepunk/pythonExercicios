from datetime import date
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Categoria: Mirin')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 20:
    print('Categoria: Sênior')
else:
    print('Master')