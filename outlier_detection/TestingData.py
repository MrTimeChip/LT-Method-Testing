from outlier_detection.OutliersInfo import OutliersInfo
from statistics import kolomogorov_smirnov_test_window
from scipy.interpolate import interp1d


class TestingData:
    def __init__(self, data_instances):
        self.__data_instances = data_instances
        self.__outliers = OutliersInfo(data_instances)

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

    def get_shift_point(self, y_other):
        main_data = self.__data_instances[0]
        main_x = [x for x in range(0, len(main_data))]
        other_x = [x for x in range(0, len(y_other))]
        main_interp = interp1d(main_x, main_data)
        other_interp = interp1d(other_x, y_other)
        x_new = [x for x in range(0, len(main_data)//5)]
        main_filtered = list(main_interp(x_new))
        other_filtered = list(other_interp(x_new))
        print(main_filtered, other_filtered, x_new)
        point = kolomogorov_smirnov_test_window(main_filtered, other_filtered).shift_point
        return point
