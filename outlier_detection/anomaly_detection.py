from outlier_detection.TestingData import TestingData
from TestResult import  TestResult


def detect_outlier(y, y_anom):
    test_data_normal = TestingData([y])
    test_data_normal.find_outliers()
    test_data_anom = TestingData([y_anom])
    test_data_anom.find_outliers()

    found_outliers = test_data_normal.are_outliers_among_data(test_data_anom.get_all_outliers())
    count = test_data_normal.get_count_difference(test_data_anom.get_outlier_count_info())
    density = test_data_normal.get_density_difference(test_data_anom.get_max_density())

    result = TestResult(found_outliers)
    result.outliers_count_compared = count
    result.outliers_density_compared = density

    result.add_shift_point(test_data_normal.get_shift_point(y_anom))

    return result
