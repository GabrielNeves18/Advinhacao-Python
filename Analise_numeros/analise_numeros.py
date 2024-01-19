#!/bin/python3
"""
Programa de Classificação e Análise de Números

Este programa solicita ao usuário uma lista de números inteiros e realiza as seguintes operações:
- Cria duas novas listas: uma contendo os números pares e outra contendo os números ímpares.
- Exibe as duas listas resultantes.
- Calcula e exibe a média dos números pares e a média dos números ímpares presentes na 
lista original.

Entrada:
    - O usuário é solicitado a fornecer uma lista de números inteiros. 
    A entrada é encerrada quando o usuário digita 'sair'.

Saída:
    - Duas listas: uma contendo números pares e outra contendo números ímpares.
    - Média dos números pares.
    - Média dos números ímpares.
"""

def criar_lista_principal():
    """
    Criação de Lista Principal
    Esta função solicita ao usuário uma lista de números inteiros. A entrada é encerrada quando o 
    usuário digita 'sair'. 
    Os números fornecidos são convertidos para inteiros e adicionados à lista principal.
    Retorno:
    - Uma lista contendo os números inteiros fornecidos pelo usuário.
    """
    print('Digite "sair" para sair')
    numeros_inteiro_lista = []
    while True:
        entrada_numero_inteiro = input('Digite o numero :')
        if entrada_numero_inteiro != 'sair':
            numeros_inteiro_lista.append(int(entrada_numero_inteiro))
        else:
            break
    return numeros_inteiro_lista

def separa_num_par_impar(lista_num):
    """
    Separação de Números Pares e Ímpares
    Esta função recebe uma lista de números inteiros e separa os números pares 
    e ímpares em duas listas distintas.
    Parâmetros:
        - lista_num: Uma lista de números inteiros.
    Retorno:
        - Uma tupla contendo duas listas:
            1. Lista dos números pares.
            2. Lista dos números ímpares.
    """
    lista_par = []
    lista_impares = []
    for numero in lista_num:
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impares.append(numero)
    return lista_par, lista_impares

def calculo_media(listas_separadas):
    """Realiza os calculos de média"""
    lista_numero_par = listas_separadas[0]
    lista_numero_impar = listas_separadas[1]
    media_par = sum(lista_numero_par)/len(lista_numero_par)
    media_impar = sum(lista_numero_impar)/len(lista_numero_impar)
    return media_par, media_impar

def main():
    """Chamadas do programa"""
    lista1 = criar_lista_principal()
    separacao = separa_num_par_impar(lista1)
    resultado_media = calculo_media(separacao)
    print(f"lista par {separacao[0]}")
    print(f"lista impar {separacao[1]}")
    print(f"Media par {resultado_media[0]}")
    print(f"Media impar {resultado_media[1]}")

main()
