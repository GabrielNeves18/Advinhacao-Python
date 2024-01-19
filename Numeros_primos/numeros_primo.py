#!/bin/python3

"""Programa que verifica se é primo"""

def verifica_numero_primo():
    """Verifica se um numero é primo"""
    divisivel = []
    verificar_numero = int(input("Digite um numero: "))
    if verificar_numero > 1:
        for i in range(2, int(verificar_numero/2) + 1):
            if verificar_numero % i == 0:
                divisivel.append(i)
        if not divisivel:
            print(f"{verificar_numero} é um número primo.")
        else:
            print(f"{verificar_numero} não é um número primo. Divisíveis por {verificar_numero}: {divisivel}")
    else:
        print("Numero inválido!!")

verifica_numero_primo()
