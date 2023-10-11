from analyzers import AccuracyAnalyzer
from analyzers import ForecastAnalyzer
from analyzers import OptimizationAnalyzer
from repositories import AnalysisRepository

class AnalysisService():
  def __init__(self, analysis_repository: AnalysisRepository, accuracy_analyzer: AccuracyAnalyzer, forecast_analyzer: ForecastAnalyzer, optimization_analyzer: OptimizationAnalyzer) -> None:
    self.repo = analysis_repository
    self.accuracy_analyzer = accuracy_analyzer
    self.forecast_analyzer = forecast_analyzer
    self.optimization_analyzer = optimization_analyzer
    pass