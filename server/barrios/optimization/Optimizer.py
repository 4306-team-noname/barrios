from typing import Any


class Optimizer:
    # pull in flight plan
    # and rates (from AccuracyAnalyzer)
    consumable: str
    rate: Any
    flightplan: Any

    def __init__(self, consumable: str, rate=None, flightplan=None):
        self.consumable = consumable
        self.rate = rate
        self.flightplan = flightplan

    def run_optimization(self):
        self.rate
        pass
