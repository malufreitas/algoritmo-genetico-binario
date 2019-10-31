import persistencia
from algoritmogenetico import algoritmo_genetico

def main():
    iteracoes = [1]
    geracoes = [10]
    populacao = [10]
    
    for p in populacao:
        for g in geracoes:
            for i in iteracoes:
                lista_resultado = []
                nomeArquivo = "Teste-{}iteracoes-{}populacao-{}geracao".format(i,p,g)
                for j in range(i):
                    lista_resultado.append(algoritmo_genetico(p,g))
                    print()
                persistencia.salvar_dados('testes/'+nomeArquivo,lista_resultado)

if __name__ == "__main__":
    main()