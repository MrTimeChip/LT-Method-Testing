import numpy
from outliers import smirnov_grubbs as grubbs
from scipy.stats import zscore, iqr


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

