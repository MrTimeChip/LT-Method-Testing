from statistics import empirical_rule
from numpy import std, mean


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

    def is_outlier(self, info_point, treat_original_as_normal=True):
        return abs(info_point.y - self.__outliers_avg) > 3 * self.__outliers_std    # using empirical rule

    def are_outliers(self, info_points, treat_original_as_normal=True):
        result = []
        for info_point in info_points:
            result.append(self.is_outlier(info_point))
        return result

    def analyze_data(self):
        amounts = []
        for data in self.__data_instances:
            outliers = empirical_rule([], data.y)
            self.__found_outliers.append(outliers)
            self.__all_outliers.extend(outliers)
            amounts.append(len(outliers))
        self.__min_count = min(amounts)
        self.__max_count = max(amounts)
        self.__count_deviation = std(amounts)

        self.__outliers_std = std(self.__all_outliers)
        self.__outliers_avg = mean(self.__all_outliers)
