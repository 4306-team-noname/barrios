from Analyzers import OptimizationAnalyzer, ForecastingAnalyzer
import pandas as pd


class AnalysisService():
    def __init__(self, forecaster: ForecastingAnalyzer, optimizer: OptimizationAnalyzer, repository) -> None:
        self.forecaster = forecaster
        self.optimizer = optimizer
        pass

    def forecast(self, df) -> pd.DataFrame:
        # in practice, we would probably add a parameter for
        # selecting the range of data, such as a date range
        print('Performing forecast analysis...')
        return self.forecaster.analyze(df)

    def optimize(self, df) -> pd.DataFrame:
        print('Performing optimization analysis...')
        return self.optimizer.analyze(df)
