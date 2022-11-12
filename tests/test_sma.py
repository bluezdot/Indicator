import os
import sys


def import_package(depth: int, is_jupyter: bool):
    if is_jupyter is False:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    else:
        current_dir = os.getcwd()
        
    parent_dir = current_dir
    while depth > 0:
        depth -= 1
        parent_dir = os.path.dirname(parent_dir)
    print(current_dir)
    print(parent_dir)
    sys.path.insert(0, parent_dir)

import_package(1, False)

from indicator import SMAIndicator
import pandas as pd
import talib
import numpy as np

sma = SMAIndicator(7)
 
df = pd.read_csv("./data/AAVE-USD.csv")

def func(d) -> np.ndarray:
    return d


i = df['price_at_time'][:50]
print(i.values.shape)
r = sma.calculate(i)

print(type(r))
print(r.shape)

a = (i for i in range(10))
