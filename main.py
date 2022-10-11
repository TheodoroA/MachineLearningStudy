import linearRegression as LinearRegression
import trainingData as TrainingData

if __name__ == '__main__':
    Ln = LinearRegression.LinearRegression()
    Td = TrainingData.TrainingData()

    Td.setData(0, 10)
    Td.setData(1, 15)
    Td.setData(2, 20)
    Td.setData(3, 25)
    Td.setData(4, 30)

    print(f"ErrorSum= {Ln.TotalError(Td)}")


