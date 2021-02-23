from outlier_detection.TestingData import TestingData


def detect_outlier(y, y_anom):
    test_data_normal = TestingData([y])
    test_data_normal.find_outliers()
    test_data_anom = TestingData([y_anom])
    test_data_anom.find_outliers()

    return test_data_normal.are_outliers_among_data(test_data_anom.get_all_outliers())
