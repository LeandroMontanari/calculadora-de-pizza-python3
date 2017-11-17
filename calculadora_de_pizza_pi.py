# -*- coding: utf-8 -*-

#==============================================================================
# CALULADORA DE PIZZA 2
#------------------------------------------------------------------------------
# PROGRAMADO POR: LEANDRO L. MONTANARI
# https://github.com/LeandroMontanari/calculadora-de-pizza-python3
#------------------------------------------------------------------------------
# ALTERADO POR: ROD LIMÃO
#   retirado os valores referentes ao preço
#   incluído a escolha de um valor para Pi
#==============================================================================
from math import pi

def main(opc):
    print('Considerando uma pizza de 30cm',end='')

    if opc == 1:
        print(', quanto você quer a pizza QUADRADA maior do que a REDONDA?')
        razao   = input('Razão: ')
        dif     = 0 if not razao else float(razao.replace(',','.'))
    else:
        print('e o valor do Pi = 3.141592653589793')
        dif = 0
                
    largura = 30
    raio    = 15
    area_q  = largura ** 2
    
    meu_pi = pi if not dif else ((area_q) * 100) / ((raio ** 2) * (100 + dif))   

    area_r = (raio ** 2) * meu_pi
    dif_qr = (area_q / area_r* 100) - 100
    dif_rq = 100 - (area_r / area_q* 100)
    
    print('\n')
    print('Área da pizza QUADRADA: {:.2f} cm²'.format(area_q))
    print('Área da pizza REDONDA: {:.2f} cm²'.format(area_r))
    print('\n')
    print('A pizza QUADRADA é {:.2f}% maior do que a pizza REDONDA.'.format(dif_qr))
    print('A pizza REDONDA é {:.2f}% menor do que a pizza QUADRADA.'.format(dif_rq))

    if opc == 1:
        print('\n')
        print('O valor calculado para Pi foi {}'.format(meu_pi), end='\n')

#==============================================================================
# valida_opcao (def = 30)
#------------------------------------------------------------------------------
# Valida o valor digitado para largura
#==============================================================================
def valida_opcao(x):
    return {
            '1': 1,
            '2': 2,
            }.get(x,0)
    
#==============================================================================
# EXECUTA função main()
#==============================================================================
if __name__ == "__main__":
    print('Escolha uma opção:')
    print('1 - Calcular o Pi pela diferença')
    print('2 - Calcular a diferença pelo Pi')
    
    opc = valida_opcao(input('Opção: '))
    
    if opc:
        main(opc)
    else:
        print('Opção inválida!')
    
    fim = input('\nPressione <Enter> para sair... ')
