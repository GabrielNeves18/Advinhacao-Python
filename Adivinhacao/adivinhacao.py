
#!/usr/bin/python3

import random


def jogoAdivinhacao():
    numAleatorio= random.randint(1, 101)
    tentativa = 1
    while True:
        numEscolhido = int(input('Digite um numero de 1 a 100: '))
        
        if (numEscolhido not in range(1,101)):
            print('Valor invalido, digite entre 1 e 100\n')
        else:
        
            if (numEscolhido < numAleatorio and numEscolhido != numAleatorio):
                print('Teste um numero maior')
                tentativa +=1
            elif(numEscolhido > numAleatorio and numEscolhido != numAleatorio):
                print('Teste um numero menor')
                tentativa +=1
            else:
                print(f'Voce acertou {numEscolhido}\nO numero aleatorio{numAleatorio}\nVocê tentou {tentativa}')
                break

jogoAdivinhacao()
