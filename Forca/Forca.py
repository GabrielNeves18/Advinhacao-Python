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

    while erros < chances:
        print("\nPalavra:", exibir_palavra(palavra_cifrada))
        print("Letras erradas:", ", ".join(lista_erros))
        letra = input("Digite uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1 and letra not in lista_erros:
            if letra in palavra_escolhida:
                for i, l in enumerate(palavra_escolhida):
                    if l == letra:
                        palavra_cifrada[i] = letra
            else:
                erros += 1
                lista_erros.append(letra)
                print(f'Você errou! Tentativas restantes: {chances - erros}')
        else:
            print("Entrada inválida. Por favor, digite uma letra válida.")

        if "_" not in palavra_cifrada:
            print("\nParabéns! Você acertou a palavra:", palavra_escolhida)
            break

    if "_" in palavra_cifrada:
        print(f'\nGame over! A palavra era: {palavra_escolhida}')

if __name__ == "__main__":
    palavra = escolha_palavra()
    cifrada = criacao_forca(palavra)
    jogo_forca(palavra, cifrada)
