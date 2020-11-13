import numpy
from outliers import smirnov_grubbs as grubbs
from scipy.stats import zscore, iqr, ttest_ind, mannwhitneyu


def empirical_rule(y, y_anom):
    anomalies = []
    avg = numpy.mean(y_anom)
    std = numpy.std(y_anom)
    t = 0
    for x in y_anom:
        if abs(x - avg) > 3 * std:
            anomalies.append((t, x))
        t += 1
    return anomalies


def z_score(y, y_anom):
    anomalies = []
    zscore_result = zscore(y_anom)
    t = 0
    for x in zscore_result:
        if x > 3:
            anomalies.append((t, y_anom[t]))
        t += 1
    return anomalies


def z_score_with_window(y, y_anom, windows_size=100):
    anomalies = []
    amount = len(y)
    window = windows_size // 2
    t = 0
    while t < amount:
        left_edge = t - window
        right_edge = t + window
        if t - window < 0:
            left_edge = 0
        if t + window > amount:
            right_edge = amount
        current_window = y_anom[left_edge: right_edge]
        zscore_result = zscore(current_window)
        window_t = 0
        for x in zscore_result:
            if x > 3:
                anomalies.append((left_edge + window_t, current_window[window_t]))
            window_t += 1
        right_edge += 1
        left_edge += 1
        t += 1
    return anomalies


def interquartile_range(y, y_anom):
    anomalies = []
    median = numpy.median(y_anom)
    itq = iqr(y_anom)
    t = 0
    for x in y_anom:
        if abs(x - median) > 1.5 * itq:
            anomalies.append((t, x))
        t += 1
    return anomalies


def grubbs_test(y, y_anom):
    anomalies = []
    indices = grubbs.max_test_indices(y_anom, alpha=.05)
    values = grubbs.max_test_outliers(y_anom, alpha=.05)
    for x, y in zip(indices, values):
        anomalies.append((x, y))
    return anomalies


def student_test(y, y_anom):
    anomalies = []
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
            anomalies.append((ind, y_anom[ind]))
        right_edge += step
    return anomalies


def mann_whitney_u_test(y, y_anom):
    anomalies = []
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
            anomalies.append((ind, y_anom[ind]))
        right_edge += step
    return anomalies