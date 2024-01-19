#!/bin/python3
"""Cálcular media"""

def entrada_numeros():
    """Entrada de numeros"""
    numeros = []
    while True:
        numero_entrada = input("numero escolhido: ")
        if numero_entrada.isnumeric() :
            numeros.append(int(numero_entrada))
        elif numero_entrada.lower() == "sair":
            break
    return numeros

def calculo_media(lista_numeros):
    """Calculos de media"""
    maior_num = max(lista_numeros)
    menor_num = min(lista_numeros)
    media = sum(lista_numeros) / len(lista_numeros)
    maiores_media = []
    for i in lista_numeros:
        if i > media:
            maiores_media.append(i)
    return media, maior_num, menor_num, maiores_media
numeros_calculos = entrada_numeros()
resultado = calculo_media(numeros_calculos)

print(resultado[0])
