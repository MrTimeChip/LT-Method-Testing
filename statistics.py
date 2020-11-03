import numpy
from scipy.stats import zscore, iqr


def empirical_rule(y, y_anom):
    anomalies = []
    avg = numpy.mean(y_anom)
    std = numpy.std(y_anom)
    t = 0
    for x in y_anom:
        t += 1
        if abs(x - avg) > 3 * std:
            anomalies.append((t, x))
    return anomalies


def z_score(y, y_anom):
    anomalies = []
    zscore_result = zscore(y_anom)
    t = 0
    for x in zscore_result:
        t += 1
        if x > 3:
            anomalies.append((t, x))
    return anomalies


def interquartile_range(y, y_anom):
    anomalies = []
    median = numpy.median(y_anom)
    itq = iqr(y_anom)
    t = 0
    for x in y_anom:
        t += 1
        if abs(x - median) > 1.5 * itq:
            anomalies.append((t, x))
    return anomalies