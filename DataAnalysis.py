data: list[float]

data = [2.71, 2.81, 2.81, 2.84, 2.84, 2.85, 2.86, 2.94, 2.95, 2.96, 2.97, 2.98, 2.98, 2.99, 3.03, 3.05, 3.05, 3.06,
        3.09, 3.11]


class Calculate(object):
    def __init__(self):
        self.dataList = data
        self.mean = 0

    def get_mean(self) -> float:
        for i in range(0, len(self.dataList)):
            self.mean += self.dataList[i]
        return self.mean/len(self.dataList)


calc = Calculate()
x = calc.get_mean()
print(x)
