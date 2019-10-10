'''
1. Gerar a população inicial.
2. Avaliar cada indivíduo da população.
3. Enquanto critério de parada não for satisfeito
faça
3.1 Selecionar os indivíduos mais aptos.
 3.2 Criar novos indivíduos aplicando os
 operadores crossover e mutação.
 3.3 Armazenar os novos indivíduos em uma
 nova população.
 3.4 Avaliar cada indivíduo da nova
 população.

 Função apitidao:
 f (x)=cos(x)∗x+2
'''

import Cromossomo
import math
import random

def calcula_qtd_bits(valor_binario):
    return 0


def decodificacao(valor_binario):
    qtd_bits = calcula_qtd_bits(valor_binario)
    valor_decimal = int(valor_binario, 2)
    return -20 + ( (20+20) * ( valor_decimal / ((2**qtd_bits)-1) ) )


def monta_valor_binario():
    return 0


def calcula_aptidao(valor_decodificado):
    return math.cos(valor_decodificado) ∗ (valor_decodificado + 2)


def gera_populacao_inicial(numero_populacao):
    lista_populacao = []

    for i in range(numero_populacao):
        valor_binario = monta_valor_binario()
        cromossomo = Cromossomo(valor_binario)
        lista_populacao.append(cromossomo)

    return lista_populacao


def algoritmo_genetico(numero_populacao, iteracoes):
    # Lista para armazenar os resultados para o gráfico
    # Guarda a melhor apitidao de Cada nova iteração
    lista_melhor_apitidao = []

    # Definicao da populacao inicial
    lista_populacao = gera_populacao_inicial(numero_populacao)


    for i in range (iteracoes):
        lista_selecionados = []

        for i in range(len(lista_populacao)):
            # Aleatoriamente escolhe dois cromossomos para comparar
            posicao = random.randint(0,len(lista_populacao))
            cromossomo_1 = lista_populacao[posicao]

            posicao = random.randint(0,len(lista_populacao))
            cromossomo_2 = lista_populacao[posicao]

            # Compara qual cromossomo é o melhor (menor apitidao)
            if cromossomo_1.apitidao < cromosso_2.apitidao:
                lista_selecionados.append(cromossomo_1)
            else:
                lista_selecionados.append(cromossomo_2)

    return lista_melhor_apitidao