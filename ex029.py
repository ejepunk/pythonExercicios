vel = float(input('A quantos KM/H esta o carro? '))
if vel <= 80:
    print('Tudo certo continue sua viagem!')
else:
    m = ((vel - 80) * 7)
    print('Vc foi multado em R${:.2f} pro estar a {}KM/H em uma via de no maximo 80KM/H'.format(m, vel))