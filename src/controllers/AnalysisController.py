from ..services.AnalysisService import AnalysisService

class AnalysisController():
  def __init__(self, analysis_service: AnalysisService) -> None:
    self.analysis_service = analysis_service
    pass