class TestResult:
    def __init__(self, anomalies):
        self.anomalies = anomalies
        self.outliers_count_compared = 0
        self.outliers_density_compared = 0
        self.shift_points = None

    def add_shift_points(self, points):
        self.shift_points = points
