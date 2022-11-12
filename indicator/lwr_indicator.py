from .base_indicator import BaseIndicator
import numpy as np


class LWRIndicator(BaseIndicator):
    def __init__(self, timeperiod: int) -> None:
        super().__init__()
        self.timeperiod = timeperiod
    


    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the LWR data from candlesticks data.

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
                Output data, which is LWR data
        """
        highesth = data[0].rolling(self.timeperiod).max() 
        lowestl = data[1].rolling(self.timeperiod).min()
        lwr = -100 * ((highesth - data[2]) / (highesth - lowestl))
        return lwr
