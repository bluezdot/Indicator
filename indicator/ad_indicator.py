from .base_indicator import BaseIndicator
from talib import AD as talib_ad
import numpy as np


class ADIndicator(BaseIndicator):
    def __init__(self) -> None:
        super().__init__()


    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the AD data from candlesticks data.

        Parameters
        ----------
            data: np.ndarray 
                Input data with shape = (4, -1)
                data = (high, low, close) or in other word:
                    data[0] = high \n
                    data[1] = low \n
                    data[2] = close
                    data[3] = Volume


        Returns
        -------
            output: np.ndarray of shape = (-1,) or pd.Series
                Output data, which is AD data
        """

        return talib_ad(data[0], data[1], data[2],data[3])