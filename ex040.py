nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('Reprovado!')
elif media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')