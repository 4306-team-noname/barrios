from ..analyzers.AccuracyAnalyzer import AccuracyAnalyzer
from ..analyzers.ForecastAnalyzer import ForecastAnalyzer
from ..analyzers.OptimizationAnalyzer import OptimizationAnalyzer
from ..repositories.AnalysisRepository import AnalysisRepository

class AnalysisService():
  def __init__(self, analysis_repository: AnalysisRepository, accuracy_analyzer: AccuracyAnalyzer, forecast_analyzer: ForecastAnalyzer, optimization_analyzer: OptimizationAnalyzer) -> None:
    self.repo = analysis_repository
    self.accuracy_analyzer = accuracy_analyzer
    self.forecast_analyzer = forecast_analyzer
    self.optimization_analyzer = optimization_analyzer
    pass