import persistencia
from algoritmogenetico import algoritmo_genetico

def main():
    lista_resultado = []
    for _ in range(10):
        lista_resultado.append(algoritmo_genetico(10,10))
    
    persistencia.salvar_dados("Teste10",lista_resultado)

    lista_resultado = []
    for _ in range(10):
        lista_resultado.append(algoritmo_genetico(10,20))
    
    persistencia.salvar_dados("Teste20",lista_resultado)
if __name__ == "__main__":
    main()