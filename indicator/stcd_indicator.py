from .base_indicator import BaseIndicator
from talib import SMA as talib_sma
import numpy as np


class STCDIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.__timeperiod = timeperiod

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the STCD (Momentum) data from the origin data (price).

        Parameters
        ----------
            data: np.ndarray with shape = (-1,) or pd.Series
                Input data: STCK data

        Returns
        -------
            output: np.ndarray with shape = (-1,) or pd.Series
                Osutput data, which is STCD data
        """
        return talib_sma(data, timeperiod=self.__timeperiod)
