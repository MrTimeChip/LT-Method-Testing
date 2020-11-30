import casegenerator
import math


def all_cases():
    step_shifts = [make_custom_step_case(x, 300, 20)
                   for x in range(300, 1500, 150)]

    step_different_angles = [make_custom_step_case(500, x, 20)
                             for x in range(100, 600, 100)]

    bumps_different_heights = [make_custom_bump_case(500, 600, x)
                               for x in range(10, 40, 5)]

    bumps_different_sizes = [make_custom_bump_case(500, x, 10)
                             for x in range(600, 1500, 150)]

    distribution_change_different_start = [
        make_custom_distribution_change_case(x, 53, 72)
        for x in range(500, 1600, 100)]

    distribution_change_different_min_max = [
        make_custom_distribution_change_case(
            1100,
            60 - math.floor(30*(1/x)),
            65 + math.floor(32*(1/x)))
        for x in range(1, 10)]

    result = [linear_no_anomaly, linear_with_outlier,
              linear_with_extreme_outliers,
              linear_with_ramp_up, linear_with_ramp_down,
              linear_with_sudden_step,
              linear_with_rise_no_anomaly, linear_with_slow_shift,
              linear_with_rise_with_bump_down, linear_with_rise_with_bump_up,
              periodic_with_negative_outliers, periodic_with_positive_outliers]

    result.extend(step_shifts)
    result.extend(step_different_angles)
    result.extend(bumps_different_heights)
    result.extend(bumps_different_sizes)
    result.extend(distribution_change_different_min_max)
    result.extend(distribution_change_different_start)
    return result


def make_custom_distribution_change_case(start, new_min, new_max):
    anom_amount = 1800-start

    def func():
        x, y = casegenerator \
            .generate_values(amount=1800) \
            .with_random() \
            .extract()
        _, y_add = casegenerator \
            .generate_values(min_value=new_min, max_value=new_max,
                             amount=anom_amount) \
            .with_random()\
            .extract()
        y_anom = y[:start] + y_add
        return x, y, x, y_anom

    result = func
    result.__name__ = f'linear_with_distribution_change_{start}_{new_min}_{new_max}'
    return result


def make_custom_bump_case(bump_start, bump_end, inc):
    over = bump_end - bump_start

    def func():
        x, y, _, _ = linear_with_rise_no_anomaly()
        x_anom, y_anom = casegenerator.empty() \
            .using(x, y) \
            .with_random(min_val=950, max_val=1050) \
            .with_step(bump_start, over, inc) \
            .with_step(bump_end, over, -inc) \
            .extract()
        return x, y, x_anom, y_anom

    result = func
    result.__name__ = f'linear_with_bump_{bump_start}_{bump_end}_{over}_{inc}'
    return result


def make_custom_step_case(start, over, inc):
    def func():
        x, y = casegenerator \
            .generate_values(amount=1800) \
            .with_random() \
            .extract()
        x_anom, y_anom = casegenerator \
            .empty() \
            .using(x, y) \
            .with_random(min_val=950, max_val=1050) \
            .with_step(after=start, over=over, diff=inc) \
            .extract()
        return x, y, x_anom, y_anom

    result = func
    result.__name__ = f'linear_with_bump_{start}_{over}_{inc}'
    return result


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
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
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
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
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
    x, y = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(0, 200, 30) \
        .extract()

    return x, y, x, y


def linear_with_slow_shift():
    x, y = casegenerator \
        .generate_values(min_value=60, max_value=63, amount=1800) \
        .with_random(min_val=995, max_val=1005) \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=995, max_val=1005) \
        .with_step(300, 1000, 10) \
        .extract()

    return x, y, x_anom, y_anom


def linear_with_rise_with_bump_down():
    x, y, _, _ = linear_with_rise_no_anomaly()
    x_anom, y_anom = casegenerator.empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(500, 100, -10) \
        .with_step(600, 100, 10) \
        .extract()
    return x, y, x_anom, y_anom


def linear_with_rise_with_bump_up():
    x, y, _, _ = linear_with_rise_no_anomaly()
    x_anom, y_anom = casegenerator.empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_step(500, 100, 10) \
        .with_step(600, 100, -10) \
        .extract()
    return x, y, x_anom, y_anom


def periodic_with_positive_outliers():
    x, y = casegenerator \
        .generate_periodic_values(period_multiplier=0.03) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random(min_val=950, max_val=1050) \
        .with_outlier(extreme_multiplier=0.5) \
        .extract()
    return x, y, x_anom, y_anom


def periodic_with_negative_outliers():
    x, y = casegenerator \
        .generate_periodic_values(period_multiplier=0.03) \
        .with_random() \
        .extract()
    x_anom, y_anom = casegenerator \
        .empty() \
        .using(x, y) \
        .with_random() \
        .with_outlier(extreme_multiplier=-0.5) \
        .extract()
    return x, y, x_anom, y_anom
