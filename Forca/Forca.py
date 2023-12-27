#!/bin/python3
"""Puxa o modulo de random"""
import random

def escolha_palavra ():
    """Escolhe a palavra da forca """
    lista_palavra = ['computador', 'hacking', 'asus', 'notebook']
    palavra_escolhida = random.randint(0, (len(lista_palavra) - 1 ))
    return lista_palavra[palavra_escolhida]


def criacao_forca(palavra):

    """
        Cria as linhas da forca
    
    """
    quantidade_linha = len(palavra)
    contador = 0
    linha_forca = []
    while contador < quantidade_linha:
        linha_forca.append("- ")
        contador +=1    
    
    return "".join(linha_forca)


def jogo_forca(palavra_escolhida, tracos):
    """Criação do jogo forca"""
    
    chances = 6
    erros = 0
    lista_erros = []
    tentativas = 0
    linhas = tracos
    
    print(linhas)
    
    
    
        
        
    
jogo_forca(escolha_palavra(), criacao_forca(escolha_palavra()))