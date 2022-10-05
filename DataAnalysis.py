import math

data: list[float]

data = [2.71, 2.81, 2.81, 2.84, 2.84, 2.85, 2.86, 2.94, 2.95, 2.96, 2.97, 2.98, 2.98, 2.99, 3.03, 3.05, 3.05, 3.06,
        3.09, 3.11]


class Calculate(object):

    def __init__(self):
        self.dataList = data
        self.data_length = len(self.dataList)

    def calculate_mean(self):
        local_mean: float = 0
        for i in range(0, self.data_length):
            local_mean += self.dataList[i]
        local_mean = local_mean / self.data_length
        return local_mean

    @property
    def get_mean(self):
        return self.calculate_mean()

    def calculate_standard_deviation(self) -> float:
        local_std_variation: float = 0
        for i in range(0, self.data_length):
            local_std_variation += math.pow((self.dataList[i] - self.get_mean), 2)
        local_std_variation = local_std_variation / (self.data_length - 1)
        local_std_variation = math.sqrt(local_std_variation)
        return local_std_variation

    @property
    def get_std_variation(self):
        return self.calculate_standard_deviation()


calc = Calculate()
y = calc.get_mean
x = calc.get_std_variation
print(x)
