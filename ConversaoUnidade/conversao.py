#!/usr/bin/python3

def conversorUnidade(opcaoUnidade):

    if (opcaoUnidade == '1'):
        fahreinheit = 32
        temperatura = float(input('Digite a temperatura: '))
        fahreinheit = 1.8 * temperatura + fahreinheit
        print(f'O valor de celsius em fahrenheit é {fahreinheit:.2f}')
        conversorUnidade(menu())

    elif (opcaoUnidade == '2'):
        quilometros = int(input('Digite a quantidade de quilometros: '))
        milhas = 1.609
        milhas = quilometros / milhas
        print(f'\nO de milhas é {milhas:.2f}\n')
        conversorUnidade(menu())

    elif (opcaoUnidade == '3'):
        quilograma = float(input('Digite o peso: '))
        libras = 2.205
        libras = quilograma * libras
        print(f'\nO valor de libras é {libras:.2f}')
        conversorUnidade(menu())
    
    elif (opcaoUnidade == '4'):
        fahreinheit = float(input('Digite a temperatura em fahreinheit: '))
        celsius = (fahreinheit - 32) / 1.8

        print(f'Celsius é {celsius:.2f}\n')
        conversorUnidade(menu())
    
    elif (opcaoUnidade == '5'):
        milhas = float(input('O valor em milhas é: '))
        quilometros = 1.609
        quilometros = milhas * quilometros

        print(f'O quilometros é {quilometros:.2f}')
        conversorUnidade(menu())
    elif (opcaoUnidade == '6'):
        libras = float(input('Digite o valor em libras: '))
        quilograma= 2.205
        quilograma = libras / quilograma
        print(f'A quilograma é {quilograma:.2f}')
    elif (opcaoUnidade == '0'):
        print('Obrigado por participar do nosso conversor!!')
    else:
        print('Opção invalida!')



def menu():
    print('Seja bem vindo ao nosso conversor de unidades\n')

    print('O que você deseja converter: ')
    print('1) Converter de Celsius para Fahreinheit\n2) Converter de quilometros e milhas\n3) Converter de quilogramas para libras\n4) Converter de Fahreinheit para Celsius\n5) Converter milhas para quilometro\n6) Converter de libras para quilogramas\n0) Sair')
    escolhaUnidade = input('>>> ')

    if (escolhaUnidade.isdigit()):
        return escolhaUnidade
    else:
        print('Valor invalido')
        conversorUnidade(menu())

conversorUnidade(menu())






