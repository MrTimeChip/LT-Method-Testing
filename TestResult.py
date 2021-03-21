class TestResult:
    def __init__(self, anomalies):
        self.anomalies = anomalies
        self.outliers_count_compared = 0
        self.outliers_density_compared = 0
        self.shift_point = None

    def add_shift_point(self, point):
        self.shift_point = point
