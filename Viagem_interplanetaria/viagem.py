#!/bin/python3
"""
    Desafio da Viagem Interplanetária

        Programa em Python para calcular a quantidade de combustível 
        necessária em uma viagem interplanetária.
        Considera a escolha do planeta de origem e destino, 
        calculando a estimativa de combustível com base
        nas distâncias médias entre eles e a eficiência do veículo espacial. 
        Também fornece informações
        adicionais como duração da viagem, velocidade média e sugestões de paradas estratégicas.

        Autor: Gabriel Neves
        Data de Criação: 23/01/2023
"""

def escolha_planetas():
    """Digite os planetas necessários para viagem"""
    planeta_origem = input("Digite o planeta origem: ")
    planeta_destino = input('Digite o planeta destino: ')
    distancia_planetas = int(input('Digite a distancia dos planetas: '))
    existencia_planetas_intermediario = input('Existe planetas intermediários: ')
    if existencia_planetas_intermediario.lower() == 'sim':
        quantidade_planeta = int(input('Digite a quantidade de planetas intermediarios: '))
        return planeta_origem, planeta_destino, distancia_planetas, quantidade_planeta
    elif existencia_planetas_intermediario.lower() == 'não':
        return planeta_origem, planeta_destino, distancia_planetas
    else:
        print('Opção errada!! Digite sim ou não')
        return escolha_planetas
planetas = escolha_planetas()
