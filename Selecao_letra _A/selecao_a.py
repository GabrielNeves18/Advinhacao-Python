#!/bin/python3
"""Programa que separa palavras com a letra A"""


def criacao_lista():
    """Cria a lista de palavra"""
    lista_palavras = []
    print("Digite 0 para terminar a lista")   
    while True:
        palavra = input("Digite uma palavra: ")
        if palavra != "0":
            lista_palavras.append(palavra)
        else:
            break
    return lista_palavras, len(lista_palavras)

def separar_lista(lista):
    """Separa as palavras com letra A"""
    palavras_inicio_a = []
    print(lista)
    for palavra in lista:
        if 'A' in palavra[0] or 'a' in palavra[0]:
            palavras_inicio_a.append(palavra)
    quantidade_palavras_a = len(palavras_inicio_a)
    return palavras_inicio_a, quantidade_palavras_a

palavras = criacao_lista()
resultado = separar_lista(palavras[0])
print(f"O total de palavra na lista original é {palavras[1]} ")
print(f"A lista resultante com letras A's é {resultado[0]}")
print(f"A quantidade de palavras com A é {resultado[1]}")
