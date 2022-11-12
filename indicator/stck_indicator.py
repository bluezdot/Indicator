from .base_indicator import BaseIndicator
from talib import STOCHF as talib_stck
import numpy as np


class STCKIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.__timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the STCK (Momentum) data from the origin data (price).

        Parameters
        ----------
            Input data with shape = (3, -1)
                data = (high, low, close) or in other word:
                    data[0] = high \n
                    data[1] = low \n
                    data[2] = close


        Returns
        -------
            output: np.ndarray with shape = (-1,) or pd.Series
                Osutput data, which is STCK data
        """
        stck, _ = talib_stck(data[0], data[1], data[2], fastk_period=self.__timeperiod, fastd_period=3, fastd_matype=0)
        return stck
