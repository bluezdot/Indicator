from .base_indicator import BaseIndicator
from talib import WMA as talib_wma
import numpy as np


class WMAIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.__timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the MOM (Momentum) data from the origin data (price).

        Parameters
        ----------
            data: np.ndarray with shape = (-1,) or pd.Series
                Input data

        Returns
        -------
            output: np.ndarray with shape = (-1,) or pd.Series
                Osutput data
        """
        return talib_wma(data, timeperiod=self.__timeperiod)
