#!/bin/python3

import random

def escolha_palavra():
    lista_palavra = ['computador', 'hacking', 'asus', 'notebook']
    palavra_escolhida = random.choice(lista_palavra)
    return palavra_escolhida

def criacao_forca(palavra):
    quantidade_linha = len(palavra)
    return ["_"] * quantidade_linha

def exibir_palavra(palavra_cifrada):
    return " ".join(palavra_cifrada)

def jogo_forca(palavra_escolhida, palavra_cifrada):
    chances = 6
    erros = 0
    lista_erros = []
    tentativas = 0
    linhas = tracos
    
    while tentativas <= chances:
        letra = input("Digite uma Letra ")
        
        if (letra not in palavra_escolhida):
            erros += 1
            lista_erros.append(letra)
            print(tracos)
            
            tentativas_restantes = chances -1
            print(f'Você tem {tentativas_restantes}\n')
        else:
            
            for indice, letra in enumerate(palavra_escolhida):
                linhas = tracos.replace(tracos[indice], letra)

            print(linhas)
            
        tentativas +=1
        
        
    
jogo_forca(escolha_palavra(), criacao_forca(escolha_palavra()))