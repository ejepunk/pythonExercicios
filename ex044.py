produto = float(input('qual o preço do produto? '))
print('qual a forma de pagamento?')
print('1 - à vista? ')
pg = int(input('2 - no cartão? '))
if pg == 1:
    print('à vista vc tem desconto de 10%')
    valor = produto - (produto * 0.1)
    print('Você tem que pagar R${:.2f} seu desconto foi de R${:.2f}'.format(valor, (produto*0.1)))
elif pg == 2:
    par = int(input('Em quantas vezes vc quer fazer:'))
    if par == 1:
        print('em {} vc tem desconto de 5%'.format(par))
        valor = produto - (produto * 0.05)
        print('Você tem que pagar R${:.2f} seu desconto foi de R${:.2f}'.format(valor, (produto * 0.05)))
    elif par == 2:
        print('em {}X não tem desconto!'.format(par))
        valor = produto
        print('Você tem que pagar R${:.2f} por parcela ficando em um total de R${:.2f} '.format((valor / par), valor))
    elif par >= 3:
        print('em {} vc tem juros de 20%'.format(par))
        valor = produto +(produto * 0.2)
        print('Você tem que pagar R${:.2f} por parcela seu juros foi de R${:.2f} ficando em um total de R${:.2f}'.format((valor / par),
                                                                                                       (produto * 0.2),
                                                                                                       valor))

