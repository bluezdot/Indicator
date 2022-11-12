from .base_indicator import BaseIndicator
from talib import CCI as talib_cci
import numpy as np


class CCIIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the CCI data from candlesticks data.

        Parameters
        ----------
            data: np.ndarray 
                Input data with shape = (3, -1)
                data = (high, low, close) or in other word:
                    data[0] = high \n
                    data[1] = low \n
                    data[2] = close

        Returns
        -------
            output: np.ndarray of shape = (-1,) or pd.Series
                Output data, which is CCI data
        """

        return talib_cci(data[0], data[1], data[2], timeperiod=self.timeperiod)
