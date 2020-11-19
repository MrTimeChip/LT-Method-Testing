import casegenerator


def all_cases():
    return [linear_no_anomaly, linear_with_outlier, linear_with_extreme_outliers,
            linear_with_ramp_up, linear_with_ramp_down, linear_with_sudden_step,
            linear_with_rise_no_anomaly, linear_with_slow_shift,
            linear_with_rise_with_bump_down, linear_with_rise_with_bump_up,
            periodic_with_negative_outliers, periodic_with_positive_outliers]


def linear_no_anomaly():
    x, y = casegenerator.generate_values(amount=1800).with_random().extract()
    return x, y, x, y


def linear_with_outlier():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y)\
        .with_random(min_val=950, max_val=1050)\
        .with_outlier(extreme_multiplier=-0.5) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_negative_outlier():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y)\
        .with_random(min_val=950, max_val=1050)\
        .with_outlier(extreme_multiplier=0.5) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_extreme_outliers():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_outlier(extreme_multiplier=0.3) \
        .extract()
    x_final, y_final = casegenerator \
        .empty() \
        .using(x_anom, y_anom) \
        .with_random(min_val=950, max_val=1050) \
        .with_outlier(extreme_multiplier=0.6) \
        .extract()
    return x_anom, y_anom, x_final, y_final


def linear_with_ramp_up():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(after=700, over=300, diff=30) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_ramp_down():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(after=700, over=300, diff=-30) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_sudden_step():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(after=0, over=1, diff=30) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_rise_no_anomaly():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x, y = casegenerator\
        .empty()\
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(0, 200, 30)\
        .extract()

    return x, y, x, y


def linear_with_slow_shift():
    x, y = casegenerator \
        .generate_values(min_value=60, max_value=63, amount=1800) \
        .with_random(min_val=995, max_val=1005) \
        .extract()
    x_anom, y_anom = casegenerator\
        .empty()\
        .using(x, y) \
        .with_random(min_val=995, max_val=1005) \
        .with_step(300, 1000, 10)\
        .extract()

    return x, y, x_anom, y_anom


def linear_with_rise_with_bump_down():
    x, y, _, _ = linear_with_rise_no_anomaly()
    x_anom, y_anom = casegenerator.empty()\
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(500, 100, -10)\
        .with_step(600, 100, 10)\
        .extract()
    return x, y, x_anom, y_anom


def linear_with_rise_with_bump_up():
    x, y, _, _ = linear_with_rise_no_anomaly()
    x_anom, y_anom = casegenerator.empty()\
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(500, 100, 10)\
        .with_step(600, 100, -10)\
        .extract()
    return x, y, x_anom, y_anom


def periodic_with_positive_outliers():
    x, y = casegenerator\
        .generate_periodic_values(period_multiplier=0.03) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator\
        .empty()\
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_outlier(extreme_multiplier=0.5)\
        .extract()
    return x, y, x_anom, y_anom


def periodic_with_negative_outliers():
    x, y = casegenerator\
        .generate_periodic_values(period_multiplier=0.03)\
        .with_random()\
        .extract()
    x_anom, y_anom = casegenerator\
        .empty()\
        .using(x, y) \
        .with_random() \
        .with_outlier(extreme_multiplier=-0.5)\
        .extract()
    return x, y, x_anom, y_anom
