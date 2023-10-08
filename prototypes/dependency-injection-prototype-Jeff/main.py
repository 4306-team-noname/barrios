from AnalysisController import AnalysisController
from AnalysisService import AnalysisService
from Analyzers import ForecastingAnalyzer, OptimizationAnalyzer


"""
Note: You probably will want a good Result class for a lot of the operations
      You're going to be doing. @see: https://aaronluna.dev/blog/error-handling-python-result-class/
"""

controller = AnalysisController(
    AnalysisService(
        ForecastingAnalyzer(),
        OptimizationAnalyzer(),
    )
)


"""
The above could have been written as:

# instantiate ForecastingAnalyzer and OptimizationAnalyzer
forecaster = ForecastingAnalyzer()
optimizer = OptimizationAnalyzer()

# instantiate AnalysisService, passing in forecaster & optimizer
analysis_service = AnalysisService(forecaster, optimizer)

# instantiate AnalysisController, passing in analysis_service
controller = AnalysisController(analysis_service)

"""

print('\n\n')
forecast = controller.get_forecast()
print(forecast)


print('\n\n')
optimization = controller.get_optimization()
print(optimization)

print("Hello World")
