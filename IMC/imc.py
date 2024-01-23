#!/bin/python3
import numpy as np
"""
Este programa em Python permite calcular o IMC com base no peso e altura fornecidos pelo usuário.

Instruções:
1. Insira o peso em quilogramas.
2. Insira a altura em metros.
3. O IMC é calculado como peso / (altura * altura).
4. Resultado do IMC é classificado conforme a tabela de classificação padrão.
   - Abaixo de 18,5: Abaixo do peso
   - 18,5 a 24,9: Peso normal
   - 25,0 a 29,9: Sobrepeso
   - 30,0 a 34,9: Obesidade grau 1
   - 35,0 a 39,9: Obesidade grau 2
   - 40,0 ou mais: Obesidade grau 3 (obesidade mórbida)
5. Exibe o resultado do IMC e a classificação correspondente.
"""


def entrada_altura_peso():
    """Entrada da altura e do peso"""
    peso = input('Digite o seu peso: ')
    altura = input('Digite a sua altura: ')
    try:
        return float(peso), float(altura)
    except ValueError:

        print("Valores inválidos, isto não é um numero")
        return entrada_altura_peso()
def calculo_imc(peso_altura):
    """Realiza o calculo"""
    return peso_altura[0] / (peso_altura[1] * peso_altura[1])
def classificacao_imc(imc):
    """Mostra qual é o seu imc"""
    peso_normal = (18.5, 24.9)
    sobrepeso = (25, 29.9)
    obesidade1 = (30, 34.9)
    obesidade2 = (35,39.9,0.1)
    if imc >= peso_normal[0] and imc <= peso_normal[1]:
        return f'Peso normal IMC = {imc:.2f}'
    elif imc >= sobrepeso[0] and imc <= sobrepeso[1]:
        return f'Sobre peso IMC = {imc:.2f}'
    elif imc >= obesidade1[0] and  imc <= obesidade1[1]:
        return f'Obesidade grau 1 IMC = {imc:.2f}'
    elif imc >= obesidade2[0] and imc <= obesidade2[1]:
        return f'Obesidade grau 2 IMC = {imc:.2f}'
    else:
        return f"Obesidade mórbida IMC = {imc:.2f}"
    
entrada_valores = entrada_altura_peso()
valor_imc = calculo_imc(entrada_valores)
resultado_imc = classificacao_imc(valor_imc)

print(resultado_imc)
