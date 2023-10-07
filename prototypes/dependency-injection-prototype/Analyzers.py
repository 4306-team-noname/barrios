from abc import ABC, abstractmethod
import pandas as pd


class AbstractAnalyzer(ABC):
    # AbstractAnalyzer defines the interface for all
    # Analyzer classes, similar to a header file definition
    # in C++.
    @abstractmethod
    # analysis will be done on a Pandas dataframe
    def analyze(self, df: pd.DataFrame):
        # not defining behavior in the interface
        pass


class ForecastingAnalyzer(AbstractAnalyzer):
    # implementation of AbstractAnalyzer
    def __init__(self) -> None:
        super().__init__()

    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        # some implementation code
        return df.head()


class OptimizationAnalyzer(AbstractAnalyzer):
    # implementation of AbstractAnalyzer
    def __init__(self) -> None:
        super().__init__()

    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        # some implementation code
        return df.tail()
