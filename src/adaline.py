from readFile import *

import numpy as np
import matplotlib.pyplot as plt


class Adaline:
    def __init__(self, trainingInputData, trainingOutputData, learningRate, precision):
        self.trainingInputData = trainingInputData
        self.trainingOutputData = trainingOutputData
        self.learningRate = learningRate
        self.precision = precision
        self.weights = np.random.uniform(0, 1, 5)
        self.startingWeights = np.array(self.weights)
        self.epochs = 0
        self.y_EQM = []
        self.x_Epochs = []

    def training(self):
        size = len(self.trainingInputData)
        previousError = float("inf")
        currentError = 0

        self.y_EQM.append(previousError)
        self.x_Epochs.append(0)

        while abs(previousError - currentError) > self.precision:
            previousError = currentError
            currentError = 0

            for i in range(size):
                x = np.array(self.trainingInputData[i])

                u = np.dot(x, self.weights)

                sampleError = self.trainingOutputData[i] - u

                self.weights = self.weights + self.learningRate * sampleError * x

                currentError += sampleError**2

            currentError /= size
            self.epochs += 1

            self.y_EQM.append(currentError)
            self.x_Epochs.append(self.epochs)

    def bipolarStepFunction(self, u):
        return 1 if u >= 0 else -1

    def operation(self, x):
        u = np.dot(x, self.weights)
        y = self.bipolarStepFunction(u)
        return y

    def EQMchart(self):
        plt.plot(
            self.x_Epochs,
            self.y_EQM,
            linestyle="-.",
            color="black",
        )

        self.y_EQM = np.where(np.isinf(self.y_EQM), 2, self.y_EQM)

        plt.ylim(0.1, 2)

        plt.title("EQM vs Épocas")
        plt.xlabel("Épocas")
        plt.ylabel("EQM")
        plt.grid()
        plt.show()

    def trainingRecord(self):
        print("Vetor de Pesos Inicial\n")

        for i in range(len(self.startingWeights)):
            print(f"w{i}: {self.startingWeights[i]:.4f}")

        print("\nVetor de Pesos Final\n")

        for i in range(len(self.weights)):
            print(f"w{i}: {self.weights[i]:.4}")

        print(f"\nNúmero de Épocas: {self.epochs}")
