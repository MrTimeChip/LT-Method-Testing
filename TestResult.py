
class TestResult:
    def __init__(self, anomalies):
        self.anomalies = anomalies
        self.is_outliers_count_exceeded = False
        self.is_outliers_density_exceeded = False
        self.shift_point = None

    def add_shift_point(self, point):
        self.shift_point = point