# Adaline - Classificação de Sinais Ruidosos

O **Adaline** (ADAptive LInear NEuron) é um algoritmo de aprendizado de máquina utilizado para a classificação de dados, especialmente eficaz em cenários com sinais ruidosos. Este algoritmo baseia-se em um modelo de rede neural simples que ajusta os pesos de forma a minimizar o erro quadrático em relação a todas as amostras disponíveis.

## 🤖 Como Funciona o Treinamento

Durante o processo de treinamento, o vetor de pesos é continuamente ajustado para reduzir o erro quadrático. Esse aspecto é crucial, pois o Adaline busca minimizar o erro em relação a todas as amostras.

> **💡 Descoberta:** Diferentes execuções do treinamento em um mesmo conjunto de dados, mesmo quando iniciadas com pesos aleatórios, tendem a convergir para pesos finais semelhantes e praticamente inalterados. Esse comportamento ocorre porque o algoritmo de treinamento busca continuamente o valor ótimo, resultando em pesos finais que são consistentes entre as várias execuções.

## Tutorial: Executando Código com `venv` no Windows, Linux e Mac

### 📘 Introdução

Este tutorial orienta você sobre como criar um ambiente virtual usando `venv` e instalar as bibliotecas `numpy` e `matplotlib` em diferentes sistemas operacionais.

### 📋 Pré-requisitos

Certifique-se de que você tenha o Python instalado em seu sistema. Você pode verificar se o Python está instalado e qual versão está utilizando com o seguinte comando:

```bash
python3 --version
```

### 1.🛠️ Clonando o Repositório

Para clonar o repositório adaline-neural-network use o comando git clone abaxio.

```bash
git clone https://github.com/Robson-Carvalho/adaline-neural-network.git
```

### 2.🌍 Criando um Ambiente Virtual

**Windows**

Abra o Prompt de Comando ou PowerShell. Navegue até o diretório onde você deseja criar o ambiente virtual:

```bash
cd adaline-neural-network
```

Crie um ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

**Linux e Mac**

Abra o Terminal. Navegue até o diretório onde você clonou o repositório:

```bash
cd adaline-neural-network
```

Crie um ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source nome_do_ambiente/bin/activate
```

### 3. 📦 Instalando as Bibliotecas Necessárias

Com o ambiente virtual ativado, você pode instalar as bibliotecas numpy e matplotlib usando pip.

```bash
pip3 install numpy matplotlib
```

### 4. 🚀 Executando o Código

Para executar o código, certifique-se de que o ambiente virtual ainda esteja ativo. Execute o arquivo Python:

```bash
python3 src/main.py
```

### 5. Desativando o Ambiente Virtual

Após finalizar seus trabalhos, você pode desativar o ambiente virtual usando o comando:

```bash
deactivate
```

🎉 Conclusão

Neste tutorial, você aprendeu como utilizar o Adaline para a classificação de sinais ruidosos e como configurar seu ambiente de desenvolvimento. Se tiver dúvidas ou precisar de assistência, sinta-se à vontade para perguntar!
