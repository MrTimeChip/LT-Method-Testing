from statistics import empirical_rule
from scipy.stats import tstd, tmean
import math


class OutliersInfo:
    def __init__(self, data_instances):
        self.__data_instances = data_instances
        self.__found_outliers = []
        self.__outliers_std = 0
        self.__outliers_avg = 0
        self.__all_outliers = []
        self.__count_deviation = 0
        self.__min_count = 0
        self.__max_count = 0
        self.__max_density = 0

    def get_all_outliers(self):
        return self.__all_outliers

    def get_outlier_count_info(self):
        return self.__count_deviation, self.__min_count, self.__max_count

    def get_max_density(self):
        return self.__max_density

    def get_density_difference(self, density):
        result = 1 - self.__max_density / density
        if result < 0:
            result -= 1
        return result

    def is_outlier(self, info_point, treat_original_as_normal=True):
        return abs(
            info_point[1] - self.__outliers_avg) > 3 * self.__outliers_std

    def are_outliers(self, info_points, treat_original_as_normal=True):
        result = []
        for info_point in info_points:
            if self.is_outlier(info_point):
                result.append(info_point)
        return result

    def get_count_difference(self, outlier_count_info):
        return self.__max_count - outlier_count_info[2]

    def analyze_data(self):
        amounts = []
        max_density = 0
        for data in self.__data_instances:
            result = empirical_rule([], data)
            self.__found_outliers.append(result.anomalies)
            self.__all_outliers.extend(result.anomalies)
            amounts.append(len(result.anomalies))
            density = self.analyze_max_density(data, result.anomalies)
            if density > max_density:
                max_density = density
        self.__min_count = min(amounts)
        self.__max_count = max(amounts)
        if len(amounts) > 1:
            self.__count_deviation = tstd(amounts)

        if len(self.__all_outliers) > 0:
            self.__outliers_std = tstd(self.__all_outliers)[1]
            self.__outliers_avg = tmean(self.__all_outliers)

        self.__max_density = max_density

    def analyze_max_density(self, data, outliers):
        data_length = len(data)
        window = 100
        left_border = 0
        max_density = 0
        step = 10
        while True:
            right_border = left_border + window
            data_slice = data[left_border:right_border]
            all_outliers_in_range = [(t, x) for t, x in outliers if
                                     left_border <= t <= right_border]
            outliers_count = len(all_outliers_in_range)
            density = outliers_count / len(data_slice)
            if density > max_density:
                max_density = density
            left_border += step
            if left_border >= data_length - 100:
                break
        return max_density
