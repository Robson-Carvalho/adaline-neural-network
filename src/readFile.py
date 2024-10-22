def getInputData():
    try:
        with open("data/training.txt", "r") as file:
            lines = file.readlines()

        inputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 6:
                inputs.append([float(num) for num in numbers[:5]])

        return inputs

    except FileNotFoundError:
        print("Erro: O arquivo data/training.txt não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getOutputData():
    try:
        with open("data/training.txt", "r") as file:
            lines = file.readlines()
        outputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 6:
                outputs.append(float(numbers[5]))

        return outputs

    except FileNotFoundError:
        print("Erro: O arquivo data/training.txt não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getTestInputData():
    try:
        with open("data/test.txt", "r") as file:
            lines = file.readlines()

        inputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 6:
                inputs.append([float(num) for num in numbers[:5]])

        return inputs

    except FileNotFoundError:
        print("Erro: O arquivo data/test.txt não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getTestOutputData():
    try:
        with open("data/test.txt", "r") as file:
            lines = file.readlines()
        outputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 6:
                outputs.append(float(numbers[5]))

        return outputs

    except FileNotFoundError:
        print("Erro: O arquivo data/training.txt não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getSamplesData():
    try:
        with open("data/samples.txt", "r") as file:
            lines = file.readlines()

        samples = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 5:
                samples.append([float(num) for num in numbers])

        return samples

    except FileNotFoundError:
        print("Erro: O arquivo data/training.txt não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []
