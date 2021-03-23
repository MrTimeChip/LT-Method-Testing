from outlier_detection.OutliersInfo import OutliersInfo
import numpy as np


class TestingData:
    def __init__(self, data_instances):
        self.__data_instances = data_instances
        self.__outliers = OutliersInfo(data_instances)
        self.__window_statistics = []

    def get_window_statistics(self):
        return list(self.__window_statistics)

    def find_outliers(self):
        self.__outliers.analyze_data()

    def is_outlier_among_data(self, info_point):
        self.__outliers.is_outlier(info_point)

    def are_outliers_among_data(self, info_points):
        return self.__outliers.are_outliers(info_points)

    def get_all_outliers(self):
        return self.__outliers.get_all_outliers()

    def get_count_difference(self, count_info):
        return self.__outliers.get_count_difference(count_info)

    def get_outlier_count_info(self):
        return self.__outliers.get_outlier_count_info()

    def get_density_difference(self, density):
        return self.__outliers.get_density_difference(density)

    def get_max_density(self):
        return self.__outliers.get_max_density()

    def get_shift_points(self, data_other):
        result = []
        data = self.__window_statistics
        amount = min(len(data_other), len(data))

        for i in range(0, amount):
            _, mean, std = data[i]
            point_other, mean_other, std_other = data_other[i]
            if abs(mean * 1.5) < abs(mean_other) and std < std_other:
                print(point_other, mean, mean_other)
                result.append(point_other)
        return result

    def calculate_window_statistics(self):
        self.__window_statistics = self.make_window_statistics(self.__data_instances[0])

    def make_window_statistics(self, data):
        result = []
        amount = len(data)
        window = 30
        step = 15
        right_edge = window
        last_window = False
        while right_edge <= amount:
            x = right_edge - window
            y = right_edge
            values = data[x:y]
            point = (x, y)
            mean = np.mean(values)
            std = np.std(values)
            result.append((point, mean, std))
            right_edge += step
            if last_window:
                break
            if right_edge > amount:
                right_edge = amount
                last_window = True
        return result
