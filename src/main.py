from readFile import *
from adaline import *

trainingInputData = getInputData()
trainingOutputData = getOutputData()
testInputData = getTestInputData()
testOutputData = getTestOutputData()
samplesData = getSamplesData()

learningRate = 0.0025
precision = 10e-6

x = int(input("Número de treinamento: "))

models = []

for i in range(0, x):
    model = Adaline(trainingInputData, trainingOutputData, learningRate, precision)
    model.training()
    models.append(model)

if models:
    for i in range(len(models)):
        print(f"Treinamento {i+1}")
        for e in range(len(samplesData)):
            print(f"Amostra {e+1}")
            print(models[i].operation(samplesData[e]))

models[0].EQMchart()
