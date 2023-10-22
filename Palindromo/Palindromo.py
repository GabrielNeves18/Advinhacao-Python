#!/bin/python3

""" Verifica se é um palindromo """

def is_palindromo() :
    """ Verifica palindromo """
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1] :
        print(f"A palavra {palavra} é um palindromo")
    else:
        print("Não é um palindromo")

is_palindromo()

