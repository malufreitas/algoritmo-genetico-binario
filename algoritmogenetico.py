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

from Cromossomo import Cromossomo
import math
import random

def mutacao(filho):
    enfermeira = ''
    for bit in filho.valor_binario:
        taxaMutacao = random.uniform(0,1)
        if(taxaMutacao <= 0.01):
            if bit == '0':
                enfermeira += '1'
            else:
                enfermeira += '0'
        else:
            enfermeira += bit            
    
    filho.valor_binario = enfermeira
    return filho

def crossover(cromossomoA,cromossomoB):
    tamanhoCromossomo = len(cromossomoA.valor_binario)
    pontoCorte = random.randint(1,tamanhoCromossomo-1)
    
    parteUmA = cromossomoA.valor_binario[:pontoCorte]
    parteDoisA = cromossomoA.valor_binario[pontoCorte:]
    parteUmB = cromossomoB.valor_binario[:pontoCorte]
    parteDoisB = cromossomoB.valor_binario[pontoCorte:]
    
    valorBinfilhoUm = parteUmA + parteDoisB
    filhoUm = Cromossomo(valorBinfilhoUm)
    filhoUm.decodificado = decodificacao(valorBinfilhoUm)
    filhoUm.apitidao = calcula_aptidao(filhoUm.decodificado)

    valorBinfilhoDois = parteUmB + parteDoisA
    filhoDois = Cromossomo(valorBinfilhoDois)
    filhoDois.decodificado = decodificacao(valorBinfilhoDois)
    filhoDois.apitidao = calcula_aptidao(filhoDois.decodificado)

    return filhoUm,filhoDois

def decodificacao(valor_binario):
    qtd_bits = len(valor_binario)
    valor_decimal = int(valor_binario, 2)
    return -20 + ( (20+20) * ( valor_decimal / ((2**qtd_bits)-1) ) )

def monta_valor_binario():
    # Tamanho do cromosso é 6(potencia) + ~3,3 (precisao)
    tamanho = 10
    cromossomo = ''
    for _ in range(tamanho):
        bit = random.randint(0,1)
        cromossomo += str(bit)

    return cromossomo

def calcula_aptidao(valor_decodificado):
    return (math.cos(valor_decodificado) * valor_decodificado) + 2

def gera_populacao_inicial(numero_populacao):
    lista_populacao = []

    for _ in range(numero_populacao):
        valor_binario = monta_valor_binario()
        cromossomo = Cromossomo(valor_binario)
        cromossomo.decodificado = decodificacao(valor_binario)
        cromossomo.apitidao = calcula_aptidao(cromossomo.decodificado)
        lista_populacao.append(cromossomo)

    return lista_populacao

def algoritmo_genetico(numero_populacao, iteracoes):
    # Lista para armazenar os resultados para o gráfico
    # Guarda a melhor apitidao de Cada nova iteração
    lista_melhor_apitidao = []

    # Definicao da populacao inicial
    lista_populacao = gera_populacao_inicial(numero_populacao)

    for _ in range (iteracoes):
        lista_selecionados = []

        for _ in range(len(lista_populacao)):
            # Aleatoriamente escolhe dois cromossomos para comparar
            posicao = random.randint(0,len(lista_populacao)-1)
            cromossomo_1 = lista_populacao[posicao]

            posicao = random.randint(0,len(lista_populacao)-1)
            cromossomo_2 = lista_populacao[posicao]

            # Compara qual cromossomo é o melhor (menor apitidao)
            if cromossomo_1.apitidao < cromossomo_2.apitidao:
                lista_selecionados.append(cromossomo_1)
            else:
                lista_selecionados.append(cromossomo_2)

        lista_populacao_nova = []

        for i in range(0,len(lista_selecionados),2):
            cromossomoA = lista_selecionados[i]            
            cromossomoB = lista_selecionados[i+1]    

            #Crossover
            taxaCrossover = random.uniform(0,1)
            if(taxaCrossover <= 0.6):
                filho1,filho2 = crossover(cromossomoA,cromossomoB)            
            else:
                filho1,filho2 = cromossomoA,cromossomoB

            #Mutação
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)

            #Novas aptidoes dos filhos
            filho1.decodificado = decodificacao(filho1.valor_binario)
            filho1.apitidao = calcula_aptidao(filho1.decodificado)

            filho2.decodificado = decodificacao(filho2.valor_binario)
            filho2.apitidao = calcula_aptidao(filho2.decodificado)
            
            #Inserção na nova população
            lista_populacao_nova.append(filho1)
            lista_populacao_nova.append(filho2)

        #Ordenação dos filhos em ordem crescente de aptidão
        auxiliar = lista_populacao_nova.copy()
        auxiliar = sorted(auxiliar , key=Cromossomo.get_apitidao)      
              
        #Removendo o pior filho
        piorFilho = lista_populacao_nova[-1].valor_binario	    

        for cromossomo in lista_populacao_nova:
            if cromossomo.valor_binario == piorFilho:
                lista_populacao_nova.remove(cromossomo)
                break

        #Ordenação dos pais em ordem crescente de aptidão
        auxiliar = lista_populacao.copy()
        lista_populacao_ordenada = sorted(auxiliar , key=Cromossomo.get_apitidao)
        melhor_pai = lista_populacao_ordenada[0]
        
        #E mantendo o melhor pai da população anterior para a próxima geração    
        lista_populacao_nova.append(melhor_pai)

        lista_populacao = lista_populacao_nova
    
        for cromossomo in lista_populacao:
            print(cromossomo.get_apitidao())
        
        print()

    return 0