from trainingData import TrainingData as Td
from linearRegression import LinearRegression as Ln


class LinearTraining:
    TrainingData = Td()
    LinearRegression = Ln()

    def Teste(self):
        self.TrainingData.setData(0, 10)
        self.TrainingData.setData(1, 15)
        self.TrainingData.setData(2, 20)
        self.TrainingData.setData(3, 25)
        self.TrainingData.setData(4, 30)

        print(f"ErrorSum= {self.LinearRegression.TotalError(Td)}")