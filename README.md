# Algoritmo PSO 

Trabalho desenvolvido para a Disciplina de Inteligência Artificial

Alunos: [Maria Luiza](https://github.com/malufreitas) e [Tarcísio Bruni](https://github.com/tarcisiobruni)

## Explicação Teórica

O Algoritmo Genético Binário representa o uso computacional da Inteligência Artificial inspirada na Teoria da Evolução das espécies de Charles Darwin. O uso de Algoritmos Genéticos projeta melhores buscas e otimizações dentro de um domínio de interesse.

A aplicação deste código consiste em tentar várias soluções começando por levantamento de alguns indíviduos escolhidos via seleção natural, no qual dentro esse grupo é realizada a aplicação de cruzamento (*crossover*) e calculado uma chance de ocorrência de mutação para o genoma (bits) nas gerações seguintes.

Os algoritmos genéticos possuem algumas características como por exemplo não ser deterministico, trabalhar com uma populaçã de soluções de maneira simultanea e utilizar apenas informações de custo e recompensa. Também são computacionalmente fáceis de serem implementados e são facilmente hibridizados com outras técnicas dentro do campo de pesquisa da Inteligência Artificial.

## Problema Proposto

O desafio proposto pelo professor é utilizar a implementação de algum algortmo genético para minimizar a função descrita abaixo:

<p align="center">
  <img  src="">
</p>

**Restrições**

Algumas observações realizadas a fim de delimitar o domínio de implementação como por exemplo:

- Assumir de x ∈ [-20,+20]
- Codificar x como vetor binário
- Criar uma população inicial com 10 indivíduos
- Usar seleção por torneio (n=2)
- Aplicar Crossover com taxa de 60% (Crossover de 1 ponto uniforme)
- Aplicar Mutação com taxa de 1%
- Usar 10 gerações e 20 gerações

## Instalação e Execução

A construção do programa utilizou a versão 3 do [Python](https://www.python.org/), então recomendamos o uso dessa mesma versão para execução do arquivo main.py. Segue link da documentação da linguagem para as instalações da versão 3:
- https://docs.python.org/3/using/index.html

Continuando...

- Faça um clone do projeto ou faça o download dos arquivos
- Por meio da linha de comando caminhe até o diretório onde se encontram os arquivos-fonte
- Execute o comando *python main.py*

O comando acima **gera** os arquivos com resultados separados pelos processamentos de número de testes , quantidade de iterações e número da população.

## Implementação

A estrutura da implementação tomou como base não somente o pseudocódigo passado pelo professor, mas também por meio de inferências/deduções com base nos materias pesquisados (referências ao final do documento). Para fins de transparência, segue o modelo de pseudocódigo que foi usado como suporte:

1- Geração da população inicial <br>
2- Avaliação de cada indivíduo data sua sequência de bits <br>
3- Loop iterativo nas partículas processando-as da seguinte forma: <br>
>- Seleção dos indivíduos mais aptos 
>- Criação de filhos no processo de crossover e mutação
>- Armazenamento de dados em uma nova população
>- Nova avaliação dos indivíduos

#### Descrição dos Arquivos:
- *main.py* - Arquivo de chamada principal onde são especificados a quantidade de testes para rodar, a quantidade de iterações do AG e quantidade de populações.
- *algoritmogenetico.py* - Arquivo com a implementação do algoritmo junto com funções de validação, que são listadas no escopo do problema.
- *Cromossomo.py* - Arquivo com a Classe que representa uma entidade Cromossomo.
> Contém os atributos de:
> - Valor binário,
> - aptidão,
> - Valor binário decodificado

- *persistencia.py* - Arquivo com funçoes para exportação dos resultados.

### Trechos mais importantes da implementação segundo o Pseudocódigo

**Populacao Inicial**

<p align="center">
  <img  src="">
</p>

**Selecao por Torneio**

<p align="center">
  <img  src="">
</p>

**Decodificação**

<p align="center">
  <img  src="">
</p>

**Cross Over**

<p align="center">
  <img  src="">
</p>

**Mutação**

<p align="center">
  <img  src="">
</p>

**Remove pior filho**

<p align="center">
  <img  src="">
</p>

**Mantem melhor pai**
<p align="center">
  <img  src="">
</p>

****
<p align="center">
  <img  src="">
</p>

## Resultados

As tabelas a seguir mostram os resultados gráficos (média e melhor) de gBest em cada iteração, processados em uma pilha de 10 testes para os casos de:

- [20 Gerações e 10 Indivíduos]()

### Referências

- Slides e Aulas em Sala
