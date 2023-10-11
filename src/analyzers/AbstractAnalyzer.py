from abc import ABC, abstractmethod
import pandas as pd

class AbstractAnalyzer():
  @abstractmethod()
  def analyze(self, df: pd.DataFrame):
    pass