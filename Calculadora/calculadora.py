#!/bin/python3

def entradaNumero():
    num = int(input('Digite o valor de notas: '))

    return num

def media(qntNotas):
    contador = 1
    soma = 0
    
    while (contador <= qntNotas):
        nota = float(input(f'Digite a nota {contador}: '))
        
        soma += nota 
        contador += 1
    
        
    media = soma / qntNotas
    
    print(f'A média das notas é {media:.2f}')

media(entradaNumero())     
    