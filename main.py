import cases
import matplotlib.pyplot as plt
import matplotlib.patches as ptchs
import statistics
import os
import notemaker


def check_method(method, plot_once=False, line_plot=False):
    all_cases = cases.all_cases()
    notemaker.note_method_name(method.__name__)
    for case in all_cases:
        x, y, x_anom, y_anom = case()
        result = method(y, y_anom)
        fig, ax = plt.subplots()
        plt.plot(y_anom)
        title = f'{method.__name__}_with_{case.__name__}'
        anom_count = 0
        for t, anom in result:
            anom_count += 1
            circle = ptchs.Circle((t, anom), edgecolor='red', fill=False)
            ax.add_patch(circle)
            if line_plot:
                plt.axvline(x=t, color='red')
            if plot_once:
                break
        path = f'results/{method.__name__}'
        if not os.path.isdir(path):
            os.mkdir(path)
        fig.canvas.set_window_title(title)
        plt.savefig(f'{path}/{title}.png')
        plt.close(fig)
        notemaker.note_case(case.__name__, anom_count)


def check_empirical_rule():
    check_method(statistics.empirical_rule)


def check_z_score():
    check_method(statistics.z_score)


def check_interquartile_range():
    check_method(statistics.interquartile_range)


def check_grubbs():
    check_method(statistics.grubbs_test)


def check_student():
    check_method(statistics.student_test, plot_once=True, line_plot=True)


def check_mwu():
    check_method(statistics.mann_whitney_u_test, plot_once=True, line_plot=True)


def check_student_window():
    check_method(statistics.student_test_window, plot_once=True, line_plot=True)


def check_mwu_window():
    check_method(statistics.mann_whitney_u_test_window, plot_once=True, line_plot=True)


if __name__ == '__main__':
    notemaker.start_notemaking()
    check_empirical_rule()
    check_z_score()
    check_interquartile_range()
    check_grubbs()
    check_student()
    check_mwu()
    check_student_window()
    check_mwu_window()
