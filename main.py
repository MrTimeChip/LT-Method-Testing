import cases
import matplotlib.pyplot as plt
import matplotlib.patches as ptchs
import statistics
import os
import notemaker
import outlier_detection.anomaly_detection


def check_method(method):
    all_cases = cases.all_cases()
    cases_amount = len(all_cases)
    case_counter = 1
    notemaker.note_method_name(method.__name__)
    print(f'{"-" * 10}Тестирую {method.__name__} на {len(all_cases)} случаях{"-" * 10}')
    for case in all_cases:
        print(f'Тест случая {case.__name__} {case_counter}/{cases_amount}')
        x, y, x_anom, y_anom = case()
        y = y[100:]  # Warm-up phase removal
        y_anom = y_anom[100:]
        result = method(y, y_anom)
        fig, ax = plt.subplots()
        plt.text(0.05,
                 0.9,
                 f'Количестов выбросов {result.outliers_count_compared} от оригинала',
                 color='red',
                 transform=ax.transAxes)
        plt.text(0.05,
                 0.8,
                 f'Максимальная плотность выбросов {result.outliers_density_compared} от оригинала',
                 color='red',
                 transform=ax.transAxes)
        normal_label = add_distribution_to_name('Normal', y)
        anom_label = add_distribution_to_name('Anomaly', y)
        plt.plot(y_anom, label=anom_label)
        plt.plot(y, label=normal_label)
        for t, _ in result.shift_points:
            plt.axvline(x=t, color='yellow')
        title = f'{method.__name__}_with_{case.__name__}'
        anom_count = 0
        for t, anom in result.anomalies:
            anom_count += 1
            circle = ptchs.Circle((t, anom), edgecolor='red', fill=False)
            ax.add_patch(circle)
        path = f'results/{method.__name__}'
        if not os.path.isdir(path):
            os.mkdir(path)
        fig.canvas.set_window_title(title)
        plt.legend(loc='best')
        plt.savefig(f'{path}/{title}.png')
        plt.close(fig)
        notemaker.note_case(case.__name__, anom_count)
        case_counter += 1


def check_empirical_rule():
    check_method(statistics.empirical_rule)


def check_z_score():
    check_method(statistics.z_score)


def check_interquartile_range():
    check_method(statistics.interquartile_range)


def check_grubbs():
    check_method(statistics.grubbs_test)


def check_student():
    check_method(statistics.student_test)


def check_mwu():
    check_method(statistics.mann_whitney_u_test)


def check_student_window():
    check_method(statistics.student_test_window)


def check_mwu_window():
    check_method(statistics.mann_whitney_u_test_window)


def check_ks():
    check_method(statistics.kolomogorov_smirnov_test)


def check_ks_window():
    check_method(statistics.kolomogorov_smirnov_test_window)


def check_outlier_detection():
    check_method(outlier_detection.anomaly_detection.detect_outlier)


def add_distribution_to_name(name, y):
    result = ''
    if statistics.shapiro_test(y):
        result = f'{name} (normal distribution)'
    else:
        result = f'{name} (NOT normal distribution)'
    return result


if __name__ == '__main__':
    notemaker.start_notemaking()
    # check_empirical_rule()
    # check_z_score()
    # check_interquartile_range()
    # check_grubbs()
    # check_student()
    # check_mwu()
    # check_student_window()
    # check_mwu_window()
    # check_ks()
    # check_ks_window()
    check_outlier_detection()
