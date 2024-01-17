#!/bin/python3

"""Programa que somará todos os numeros pares de uma lista""" 

def entrada_lista():
    """Entrada da lista"""
    numeros = []
    while True:
        print("Digite sair para parar a lista: ")
        entrada_valor= input('Digite uma lista de numero: ')
        if entrada_valor == "sair":
            break
        else:
            numeros.append(int(entrada_valor))

    return numeros


lista = entrada_lista()

def soma_par(lista_numeros):
    """Realiza a soma dos numeros pares"""
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

total = soma_par(lista)

print(total)
