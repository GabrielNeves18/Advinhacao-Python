#!/bin/python3
"""Verifica qual é a palavra mais longa em uma lista"""
def entrada_palavra ():
    """Entrada e criação da lista de palavras"""
    lista_palavra = []
    while True:
        palavra_solicitada = input('Digite a palavra: ').lower()
        if palavra_solicitada != "sair":
            lista_palavra.append(palavra_solicitada)
        else:
            break
    return lista_palavra

def definindo_tamanho(lista):
    """Conta o tamanho da lista""" 
    tamanho_maior_palavra = []
    maior_palavra = []
    for tamanho_palavra in lista:
        tamanho_maior_palavra.append(len(tamanho_palavra))
    for tamanho in tamanho_maior_palavra:
        if tamanho == max(tamanho_maior_palavra):
            for palavras in lista:
                if len(palavras) == max(tamanho_maior_palavra):
                    maior_palavra.append(palavras)
    return maior_palavra[0]
palavras_escolhidas = entrada_palavra()
palavra = definindo_tamanho(palavras_escolhidas)

print(palavra)
