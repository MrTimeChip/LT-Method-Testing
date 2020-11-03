import casegenerator


def all_cases():
    return [linear_normal, linear_with_outlier, linear_with_extreme_outliers,
            linear_with_ramp_up, linear_with_ramp_down, linear_with_sudden_step]


def linear_normal():
    x, y = casegenerator.generate_values(amount=1800).with_random().extract()
    return x, y, x, y


def linear_with_outlier():
    x, y = casegenerator \
        .generate_values(amount=1800) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_outlier(extreme_multiplier=1.3) \
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
        .with_outlier(extreme_multiplier=1.05) \
        .extract()
    x_final, y_final = casegenerator \
        .empty() \
        .using(x_anom, y_anom) \
        .with_outlier(extreme_multiplier=1.4) \
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
        .with_step(after=0, over=1, diff=30) \
        .extract()
    return x, y, x_anom, y_anom
