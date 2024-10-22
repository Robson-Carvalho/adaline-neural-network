# Adaline - Classificação de Sinais Ruidosos

O **Adaline** (ADAptive LInear NEuron) é um algoritmo de aprendizado de máquina utilizado para a classificação de dados, especialmente eficaz em cenários com sinais ruidosos. Este algoritmo baseia-se em um modelo de rede neural simples que ajusta os pesos de forma a minimizar o erro quadrático em relação a todas as amostras disponíveis.

## Como Funciona o Treinamento

Durante o processo de treinamento, o vetor de pesos é continuamente ajustado para reduzir o erro quadrático. Esse aspecto é crucial, pois o Adaline busca minimizar o erro em relação a todas as amostras.

> **Descoberta:** Diferentes execuções do treinamento em um mesmo conjunto de dados, mesmo quando iniciadas com pesos aleatórios, tendem a convergir para pesos finais semelhantes e praticamente inalterados. Esse comportamento ocorre porque o algoritmo de treinamento busca continuamente o valor ótimo, resultando em pesos finais que são consistentes entre as várias execuções.
