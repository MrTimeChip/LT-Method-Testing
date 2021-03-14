from outlier_detection.OutliersInfo import OutliersInfo


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

    def is_outliers_count_different(self, count_info):
        return self.__outliers.is_outlier_count_different(count_info)

    def get_outlier_count_info(self):
        return self.__outliers.get_outlier_count_info()

    def is_density_exceeded(self, density):
        return self.__outliers.is_density_exceeded(density)

    def get_max_density(self):
        return self.__outliers.get_max_density()
