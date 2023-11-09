from abc import ABC, abstractmethod
import pandas as pd


class AbstractAnalyzer(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame):
        pass

