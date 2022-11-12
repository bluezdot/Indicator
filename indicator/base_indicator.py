import abc
import numpy as np

class BaseIndicator(abc.ABC):
    """
    Create an abstract class for creating object Indicator
    """

    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def calculate(self, data: np.ndarray) -> np.ndarray:
        """
        You must carefully note the type and shape of data for calculate function
        
        Parameters
        ----------
            data: np.ndarray
                Input data
            
        Returns
        -------
            output: np.ndarray
                Output data
        """        
        pass


