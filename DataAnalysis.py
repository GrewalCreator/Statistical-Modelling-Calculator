import math


class Calculate(object):

    def __init__(self, data):
        self.dataList = data
        self.data_length = len(self.dataList)
        self.quartile_data: list[float] = []

    def calculate_mean(self) -> float:
        local_mean: float = 0
        for i in range(0, self.data_length):
            local_mean += self.dataList[i]
        local_mean = local_mean / self.data_length
        return local_mean

    @property
    def get_mean(self) -> float:
        return self.calculate_mean()

    def calculate_standard_deviation(self) -> float:
        local_std_variation: float = 0
        for i in range(0, self.data_length):
            local_std_variation += math.pow((self.dataList[i] - self.get_mean), 2)
        local_std_variation = local_std_variation / (self.data_length - 1)
        local_std_variation = math.sqrt(local_std_variation)
        return local_std_variation

    @property
    def get_std_variation(self) -> float:
        return self.calculate_standard_deviation()

    def calculate_quartile(self) -> list[float]:

        list_first_half = self.get_sorted_data[0:int(len(self.get_sorted_data) / 2)]
        list_second_half = self.get_sorted_data[int(len(self.get_sorted_data)/2): len(self.get_sorted_data)]

        midQ: float = self.calculate_median(self.get_sorted_data)
        lowerQ: float = self.calculate_median(list_first_half)
        upperQ: float = self.calculate_median(list_second_half)

        self.quartile_data.append(lowerQ)
        self.quartile_data.append(midQ)
        self.quartile_data.append(upperQ)

        return self.quartile_data

    @property
    def get_all_quartiles(self) -> list[float]:
        return self.calculate_quartile()

    @staticmethod
    def calculate_median(local_list: list[float]) -> float:
        median: float = -1
        local_list_length = len(local_list)

        if local_list_length % 2 == 0:
            median = (local_list[int(local_list_length / 2)] + local_list[int((local_list_length / 2)) + 1]) / 2
        elif local_list_length % 2 == 1:
            median = (local_list_length + 1) / 2

        return median

    def get_median(self):
        return self.calculate_median(self.get_sorted_data)

    @property
    def get_sorted_data(self):
        return sorted(self.dataList)


def main():
    data: list[float] = [2.71, 2.81, 2.81, 2.84, 2.84, 2.85, 2.86, 2.94, 2.95, 2.96, 2.97, 2.98, 2.98, 2.99, 3.03,
                         3.05, 3.05, 3.06, 3.09, 3.11]

    calc = Calculate(data)

    print(calc.get_all_quartiles)
    print(calc.get_median())


if __name__ == "__main__":
    main()
