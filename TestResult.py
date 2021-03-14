
class TestResult:
    def __init__(self, anomalies):
        self.anomalies = anomalies
        self.is_outliers_count_exceeded = False
        self.is_outliers_density_exceeded = False
