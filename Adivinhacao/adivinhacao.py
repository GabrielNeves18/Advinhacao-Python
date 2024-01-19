#!/usr/bin/python3
"""Jogo de adivinhar"""

import random
def jogo_advinhacao():
    """Jogo completo"""
    num_aleatorio= random.randint(1, 101)
    tentativa = 1
    while True:
        num_escolhido = int(input('Digite um numero de 1 a 100: '))
        if num_escolhido not in range(1,101):
            print('Valor invalido, digite entre 1 e 100\n')
        else:
            if (num_escolhido < num_aleatorio and num_escolhido != num_aleatorio):
                print('Teste um numero maior')
                tentativa +=1
            elif(num_escolhido > num_aleatorio and num_escolhido != num_aleatorio):
                print('Teste um numero menor')
                tentativa +=1
            else:
                print(f"""Voce acertou {num_escolhido}\nO numero aleatorio {num_aleatorio}
                    \nVocê tentou {tentativa}""")
                break

jogo_advinhacao()
