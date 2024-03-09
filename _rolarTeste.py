import math
from _rolarDados import *


def rolar_teste():
    # pedir as quatro variáveis do teste
    while True:
        try:
            acao = int(input("Informe o Valor de Ação: "))
        except:
            print("Digite um número inteiro")
            continue
        break
    while True:
        try:
            oposicao = int(input("Informe o Valor de Oposição: "))
        except:
            print("Digite um número inteiro")
            continue
        break
    while True:
        try:
            efeito = int(input("Informe o Valor de Efeito: "))
        except:
            print("Digite um número inteiro")
            continue
        break
    while True:
        try:
            resistencia = int(input("Informe o Valor de Resistência: "))
        except:
            print("Digite um número inteiro")
            continue
        break
    # rolar os dados chamando a função
    dados = rolar_dados()
    # fazer ação - oposição + dados rolados para comparar abaixo
    acao_oposicao = acao - oposicao + dados
    # efeito final é efeito menos resistência, mais 1/2 do excesso de 11 no teste
    efeito_resistencia = efeito - resistencia + (math.floor((acao_oposicao - 11) / 2))
    # verificar se o teste foi melhor ou igual a 11 para ver o sucesso
    if acao_oposicao >= 11:
        sucesso = 'Sucesso'
        # ver se efeito é menor que zero e transformar em zero
        if efeito_resistencia < 0:
            resultado = 0
        else:
            # o efeito máximo deve ser igual ao valor de efeito
            if efeito_resistencia > efeito:
                resultado = efeito
            else:
                resultado = efeito_resistencia
    else:
        sucesso = 'Fracasso'
        resultado = 0
    print(f'\nTotal da Ação = {acao_oposicao}')
    print(f'Desfecho da Ação = {sucesso}')
    if sucesso == "Fracasso":
        print(f'Sem Resultado.')
    else:
        print(f'Pontos de Resultado: {resultado}')
