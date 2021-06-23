## Bem vindo!

Meu nome é Erick e estou cursando o 3º ano do Bacharelado em Física na USP. Desde 2019 venho fazendo alguns projetos em Python e decidi colocá-los todos em um mesmo canto. Abaixo estão os principais.

&nbsp;  
# Projeto 2: Gráficos/Estatística

Neste projeto, desenvolvi um código que, a partir de dados de um arquivo .txt, desenha uma reta que liga os pontos dos gráficos de maneira que os parâmetros da função y = ax + b são os melhores possíveis. A reta que melhor se aproxima dos pontos experimentais é aquela que minimiza o chamado "chi quadrado", muito conhecido em Estatística. Assim, é possível encontrar os parâmetros "a" e "b" de tal modo que minimizem o chi quadrado. O resultado é mostrado logo abaixo.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/filtro%20de%20wien.png?raw=True" height="300" width="420">
</p>

Através [desse link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) é possível encontrar o código fonte desse projeto (grafico_data1.py).

&nbsp;  
# Projeto 3: Captura de Pokémons

Este projeto simulou a captura de pokémons através do lançamento de pokébolas em um planeta cuja aceleração da gravidade vale 2 m/s^2 (2 metros por segundo ao quadrado). A ideia aqui é imprimir uma matriz simulando a trajetória da pokébola e contendo a posição do treinador (a pessoa que arremessa a pokébola) e do pokémon, considerando também o tamanho do pokémon. Dados como tamanho (em números de linhas e colunas), nome (por exemplo, "Nidoran") e posição do pokémon (posição na matriz) são retirados de um arquivo .txt, e o usuário do programa define a velocidade inicial e o ângulo de arremesso da pokébola.
Na imagem abaixo vemos um exemplo de saída desse programa.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/pokemon.png?raw=True" height="450" width="320">
</p>

Na imagem: o "T" representa a posição do treinador, o "0" é a trajetória da pokébola e os números de 1 a 3 na matriz representam os diferentes pokémons.
Através [desse link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) é possível encontrar o código fonte desse projeto (pokemon.py).

&nbsp;  
# Projeto 4: Modelo SIR

O modelo SIR (suscetíveis, infectados e recuperados) trata da modelagem estatística de uma população sujeita a uma doença como a Covid-19, onde a doença é transmitida através do ar. O modelo matemático é desenvolvido utilizando-se conceitos de probabilidade e estatística. Abaixo vemos uma representação desse modelo (simples) que considera apenas a taxa de infecção e a taxa de recuperação. As condições iniciais do problema são: há 99 pessoas suscetíveis e 1 pessoa infectada.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/SIR%20model.png?raw=True" height="300" width="420">
</p>

Através [desse link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) é possível encontrar o código fonte desse projeto (SIR model.py).

&nbsp;  
# Projeto 5: Partícula em uma caixa

Considere o problema de um elétron em uma caixa cúbica de aresta de tamanho L, se movendo ao longo de uma só aresta (1D), sujeito a um potencial V(x) = ax/L. A ideia aqui é encontrar a distribuição de probabilidades para o elétron utilizando conceitos de Mecânica Quântica. 

A imagem abaixo mostra os gráficos das curvas de probabilidade para um elétron se movendo ao longo do eixo x. Há pontos de maior e menor probabilidade de se encontrar a partícula em um determinado ponto da caixa. Os gráficos foram gerados para os três primeiros estados.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/particle%20in%20a%20box-3.png?raw=True" height="300" width="420">
</p>

Através [desse link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) é possível encontrar o código fonte desse projeto (hamiltoniana.py).
