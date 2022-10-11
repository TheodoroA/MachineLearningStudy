class TrainingData:
    data = dict([])

    def setData(self, x, y):
        self.data[x] = y

    def getData(self, x):
        return self.data[x]
