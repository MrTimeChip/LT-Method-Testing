import numpy
from TestResult import TestResult
from outliers import smirnov_grubbs as grubbs
from scipy.stats import zscore, iqr, ttest_ind, mannwhitneyu, ks_2samp, shapiro


def empirical_rule(y, y_anom):
    anomalies = []
    avg = numpy.mean(y_anom)
    std = numpy.std(y_anom)
    t = 0
    for x in y_anom:
        if abs(x - avg) > 3 * std:
            anomalies.append((t, x))
        t += 1
    return TestResult(anomalies)


def z_score(y, y_anom):
    anomalies = []
    zscore_result = zscore(y_anom)
    t = 0
    for x in zscore_result:
        if x > 3:
            anomalies.append((t, y_anom[t]))
        t += 1
    return TestResult(anomalies)


def interquartile_range(y, y_anom):
    anomalies = []
    median = numpy.median(y_anom)
    itq = iqr(y_anom)
    t = 0
    for x in y_anom:
        if abs(x - median) > 1.5 * itq:
            anomalies.append((t, x))
        t += 1
    return TestResult(anomalies)


def grubbs_test(y, y_anom):
    anomalies = []
    indices = grubbs.max_test_indices(y_anom, alpha=.05)
    values = grubbs.max_test_outliers(y_anom, alpha=.05)
    for x, y in zip(indices, values):
        anomalies.append((x, y))
    return TestResult(anomalies)


def student_test(y, y_anom):
    test_result = TestResult([])
    alpha = 0.05
    t, p = ttest_ind(y, y_anom)
    if p < alpha:
        test_result.add_shift_point((0, y_anom[0]))
        return test_result
    return test_result


def mann_whitney_u_test(y, y_anom):
    test_result = TestResult([])
    alpha = 0.05
    t, p = mannwhitneyu(y, y_anom)
    if p < alpha:
        test_result.add_shift_point((0, y_anom[0]))
        return test_result
    return test_result


def student_test_window(y, y_anom):
    test_result = TestResult([])
    amount = len(y_anom)
    window = amount // 30
    step = window // 2
    right_edge = window
    alpha = 0.05
    while right_edge < amount:
        values_y = y[right_edge - window:right_edge]
        values_y_anom = y_anom[right_edge - window:right_edge]
        t, p = ttest_ind(values_y, values_y_anom)
        if p < alpha:
            ind = right_edge - window
            test_result.add_shift_point((ind, y_anom[ind]))
        right_edge += step
    return test_result


def mann_whitney_u_test_window(y, y_anom):
    test_result = TestResult([])
    amount = len(y_anom)
    window = amount // 30
    step = window // 2
    right_edge = window
    alpha = 0.05
    while right_edge < amount:
        values_y = y[right_edge - window:right_edge]
        values_y_anom = y_anom[right_edge - window:right_edge]
        t, p = mannwhitneyu(values_y, values_y_anom)
        if p < alpha:
            ind = right_edge - window
            test_result.add_shift_point((ind, y_anom[ind]))
        right_edge += step
    return test_result


def kolomogorov_smirnov_test(y, y_anom):
    test_result = TestResult([])
    alpha = 0.05
    t, p = ks_2samp(y, y_anom)
    if p < alpha:
        test_result.add_shift_point((0, y_anom[0]))
        return test_result
    return test_result


def kolomogorov_smirnov_test_window(y, y_anom):
    test_result = TestResult([])
    amount = len(y_anom)
    window = amount // 30
    step = window // 2
    right_edge = window
    alpha = 0.05
    while right_edge < amount:
        values_y = y[right_edge - window:right_edge]
        values_y_anom = y_anom[right_edge - window:right_edge]
        t, p = ks_2samp(values_y, values_y_anom)
        if p < alpha:
            ind = right_edge - window
            test_result.add_shift_point((ind, y_anom[ind]))
        right_edge += step
    return test_result


def shapiro_test(y):
    alpha = 0.05
    t, p = shapiro(y)
    return p >= alpha
