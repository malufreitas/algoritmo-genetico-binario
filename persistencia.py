import statistics
from Cromossomo import Cromossomo

def salvar_dados(nome_arquivo,lista_resultado):    
    precisao_casas_decimais = 6
    
    with open(nome_arquivo + ".csv", "w") as arquivo:
        #Cabeçalho
        arquivo.write(" ")
        for i in range(len(lista_resultado)):
            arquivo.write("Execucao" + str(i+1) + " ")        
        arquivo.write("Media"+ " ")
        arquivo.write("Melhor" + " ")
        arquivo.write('\n')

        #Conteudo
        for i in range(len(lista_resultado[0])):
            data = []
            arquivo.write(str(i + 1) + "ªMelhorApt ")
            for lista in lista_resultado:
                particula_global = round(lista[i].aptidao,4)
                particula_global = round(particula_global,precisao_casas_decimais)
                data.append(particula_global)
                arquivo.write(str(particula_global).replace('.',',') + " ")

            lista = sorted(data , key=lambda t: t)
            
            #Media
            media = round(statistics.mean(data),4)
            arquivo.write(str(media).replace('.',',') + " ")

            #Melhor
            menor = round(lista[0],4)
            arquivo.write(str(menor).replace('.',',') + " ")

            # #xBest
            # xBest = lista[0].x_best
            # arquivo.write(str(xBest).replace('.',',') + " ")

            arquivo.write('\n')