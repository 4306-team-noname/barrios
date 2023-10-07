import pandas as pd
from AnalysisService import AnalysisService

# in practice, we would use a repository
# or model to query the necessary data from a
# database and convert it into a pandas DataFrame
# for this prototype, we'll just read the data from
# a flat csv file
df = pd.read_csv(
    '../../data/csv/rsa_consumable_water_summary_20220103-20230828.csv')


class AnalysisController:
    def __init__(self, analysis_service: AnalysisService) -> None:
        self.analysis_service = analysis_service
        pass

    def get_optimization(self) -> pd.DataFrame:
        return self.analysis_service.optimize(df)

    def get_forecast(self) -> pd.DataFrame:
        return self.analysis_service.forecast(df)
