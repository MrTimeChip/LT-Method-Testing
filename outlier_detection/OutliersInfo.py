from statistics import empirical_rule
from scipy.stats import tstd, tmean


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

    def get_all_outliers(self):
        return self.__all_outliers

    def get_outlier_count_info(self):
        return self.__count_deviation, self.__min_count, self.__max_count

    def is_outlier(self, info_point, treat_original_as_normal=True):
        return abs(info_point[1] - self.__outliers_avg) > 3 * self.__outliers_std

    def are_outliers(self, info_points, treat_original_as_normal=True):
        result = []
        for info_point in info_points:
            if self.is_outlier(info_point):
                result.append(info_point)
        return result

    def is_outlier_count_different(self, outlier_count_info):
        return self.__max_count + self.__count_deviation < outlier_count_info[2]

    def analyze_data(self):
        amounts = []
        for data in self.__data_instances:
            outliers = empirical_rule([], data)
            self.__found_outliers.append(outliers)
            self.__all_outliers.extend(outliers)
            amounts.append(len(outliers))
        self.__min_count = min(amounts)
        self.__max_count = max(amounts)
        if len(amounts) > 1:
            self.__count_deviation = tstd(amounts)

        self.__outliers_std = tstd(self.__all_outliers)[1]
        self.__outliers_avg = tmean(self.__all_outliers)
