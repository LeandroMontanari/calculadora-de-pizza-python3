################################################
##### PROGRAMADO POR: LEANDRO L. MONTANARI #####
################################################

from math import pi

print('Quantos centímetros tem a pizza que você quer calcular a diferença de área entre QUADRADA e REDONDA?', end='\n')
print('Por exemplo, para informar 30 cm, digite apenas o número 30 e pressione <Enter>.')
pizza = int(input('Digite: '))

print('\nQuer informar também o valor da pizza em reais, para calcular o preço por cm²?')
print('Digite 0 para não informar, ou digite o valor em reais, separando as casas decimais por ponto ao invés de vírgula.')
print('Por exemplo, se a pizza custar R$ 49,90 (quarenta e nove reais e noventa centavos), você deve digitar 49.90 e pressionar <Enter>.')
valor = float(input('Digite: R$ '))

area_quadrada = pizza ** 2
area_redonda = ((pizza / 2) ** 2) * pi
dif_qr = (area_quadrada / area_redonda * 100) - 100
dif_rq = 100 - (area_redonda / area_quadrada * 100)

valor_quadrada_cq = (valor / area_quadrada) if valor != 0 else 0
valor_redonda_cq = (valor / area_redonda) if valor != 0 else 0
cq_pq = (1 / valor_quadrada_cq) if valor != 0 else 0
cq_pr = (1 / valor_redonda_cq) if valor != 0 else 0

print('\nConsiderando o valor de Pi como {}, estes são os resultados da sua pizza de {} cm'.format(pi, pizza), end='')
if valor != 0:
    print(' que custa R$ {:.2f}'.format(valor), end='')
print(':')
print('\nÁrea da pizza QUADRADA de {} cm: {:.2f} cm²'.format(pizza, area_quadrada), end='\n')
print('Área da pizza REDONDA de {} cm: {:.2f} cm²'.format(pizza, area_redonda), end='\n\n')

print('A pizza QUADRADA é {:.2f}% maior do que a pizza REDONDA.'.format(dif_qr), end='\n')
print('A pizza REDONDA é {:.2f}% menor do que a pizza QUADRADA.'.format(dif_rq), end='\n')

if valor != 0:
    print('\nO custo por cm² da pizza QUADRADA é {:.3f} centavos.'.format(valor_quadrada_cq), end='\n')
    print('Ou seja, cada 1 centavo paga {:.1f} cm² dela.'.format(cq_pq))
    print('\nO custo por cm² da pizza REDONDA é {:.3f} centavos.'.format(valor_redonda_cq))
    print('Ou seja, cada 1 centavo paga {:.1f} cm² dela.'.format(cq_pr))

fim = input('\nPressione <Enter> para sair... ')
