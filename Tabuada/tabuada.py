#!/bin/python3

"""Tabuada de um numero"""

def numero_escolhido ():
    """Entrada do valor"""
    try:
        return int(input("digite o numero que você deseja a tabuada: "))
    except ValueError:
        print("Esse não é inteiro. Digite um numero inteiro")
        return numero_escolhido()

def tabuada(num):
    """Calcula e mostra a tabuada"""
    for multiplicador in range(0+1, 10+1) :
        print(f"{num} x {multiplicador} =",num * multiplicador, end="\n")

numero = numero_escolhido()
tabuada(numero)
