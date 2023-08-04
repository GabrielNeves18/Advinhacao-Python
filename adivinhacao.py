#!/usr/bin/python3

import random
numAleatorio = random.randint(1, 101)


def adivinhacao(numEscolhido, numAleatorio):
    if (numEscolhido < numAleatorio and  numEscolhido != numAleatorio):
        print('Tente outro numero maior!\n')
        
        entradaNum(numAleatorio)

    elif (numEscolhido > numAleatorio and numEscolhido != numAleatorio):
        print('Tente outro numero menor!\n')
        entradaNum(numAleatorio)

    else:
        print(f'Você acertou {numEscolhido}\nO numero aleatorio eh {numAleatorio}')
        


def entradaNum(numAle):
    numUser = int(input('Digite um numero de 1 a 100: '))

    if (numUser not in range(1,101)):
        print('Valor invalido, digite entre 1 e 100\n')
    else:
        adivinhacao(numUser, numAle)
        

entradaNum(numAleatorio)
