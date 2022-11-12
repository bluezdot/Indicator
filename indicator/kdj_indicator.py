from .base_indicator import BaseIndicator
import numpy as np
import pandas as pd



class KDJIndicator(BaseIndicator):
    def __init__(self) -> None:
        super().__init__()

    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        Calculate the kdj data from candlesticks data.

        Parameters
        ----------
            data: np.ndarray
                Input data with shape = (-1, 3)
                data = (high, low, close) or in other word:
                    data[0] = high \n
                    data[1] = low \n
                    data[2] = close

        Returns
        -------
            output: tuple[np.ndarray, np.ndarray, np.ndarray] or tuple[pd.Series, pd.Series, pd.Series]
                Output data, which is (K, D, J) data
                Shape of output: (3, -1)
        """
        L9 = data[1].rolling(9).min()
        H9 = data[0].rolling(9).max()
        RSV = 100 * ((data[2] - L9) / (H9 - L9)).values

        k0 = 50
        k_out = []
        for j in range(len(RSV)):
            if RSV[j] == RSV[j]:  # check for nan
                k0 = 2 / 3 * k0 + 1 / 3 * RSV[j]
                k_out.append(k0)
            else:
                k_out.append(np.nan)

        d0 = 50
        d_out = []
        for j in range(len(RSV)):
            if k_out[j] == k_out[j]:
                d0 = 2 / 3 * d0 + 1 / 3 * k_out[j]
                d_out.append(d0)
            else:
                d_out.append(np.nan)

        j_out = (3 * np.array(k_out)) - (2 * np.array(d_out))
        return k_out, d_out, j_out