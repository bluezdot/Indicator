from .base_indicator import BaseIndicator
from talib import ADX as talib_adx
import numpy as np


class ADXIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the ADX data from candlesticks data.

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
                Output data, which is ADX data
        """

        return talib_adx(data[0], data[1], data[2], timeperiod=self.timeperiod)
