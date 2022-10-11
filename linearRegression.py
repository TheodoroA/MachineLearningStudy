class LinearRegression:
    Th0 = 0.0
    Th1 = 1.0
    X = 0

    def LinearFunction(self):
        return self.Th0 + self.Th1 * self.X

    def Th0Dv(self):
        return self.Th0 + self.Th1 * self.X

    def Th1Dv(self):
        return (self.Th0 + self.Th1 * self.X) * self.X

    def TotalError(self, training_data):
        error_sum = 0
        for td in training_data.data:
            self.X = td
            error_sum += pow(training_data.getData(td) - self.LinearFunction(), 2)

        return error_sum

