import cases
import matplotlib.pyplot as plt
import matplotlib.patches as ptchs
import statistics


def check_method(method):
    all_cases = cases.all_cases()
    for case in all_cases:
        x, y, x_anom, y_anom = case()
        result = method(y, y_anom)
        fig, ax = plt.subplots()
        plt.plot(y_anom)
        fig.canvas.set_window_title(f'{method.__name__}_with_{case.__name__}')
        for t, anom in result:
            circle = ptchs.Circle((t, anom), edgecolor='red', fill=False)
            ax.add_patch(circle)
        plt.show()


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


if __name__ == '__main__':
    #check_empirical_rule()
    #check_z_score()
    #check_interquartile_range()
    #check_grubbs()
    check_student()
