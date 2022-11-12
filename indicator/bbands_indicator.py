from .base_indicator import BaseIndicator
from talib import BBANDS as talib_bbands
import numpy as np


class BBANDSIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> tuple:
        """
        Calculate the BBANDS (Bollingers Band) data from the origin data (price or close price).

        Parameters
        ----------
            data: np.ndarray with shape = (-1,) or pd.Series
                Input data

        Returns
        -------
            output: tuple[np.ndarray, np.ndarray, np.ndarray] or tuple[pd.Series, pd.Series, pd.Series]
                Output data, which is (upper, middle, lower) data
                Shape of output: (3, -1)
        """
        return talib_bbands(data, timeperiod=self.timeperiod, nbdevup=2, nbdevdn=2, matype=0)
