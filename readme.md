# Indicator Utility

## To do tasks

## Indicators
We'll split indicators into 2 groups:
### Group 1: Indicators based on only close price


#### SMA
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: np.ndarray with shape = (-1,) or pd.Series

#### EMA
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: np.ndarray with shape = (-1,) or pd.Series

#### BBANDS
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: tuple[np.ndarray, np.ndarray, np.ndarray] or tuple[pd.Series, pd.Series, pd.Series]
    + Output data, which is (upper, middle, lower) data
    + Shape of output: (3, -1)


#### MOM 
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: np.ndarray with shape = (-1,) or pd.Series

#### WMA
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: np.ndarray with shape = (-1,) or pd.Series

#### RSI
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (close) price
+ output: np.ndarray with shape = (-1,) or pd.Series

### Group 2: Indicators based on high, low, close price (and volumn) 

#### ADX
+ input: np.ndarray with shape = (3, -1)
    + data = (high, low, close) price:
        + data[0] = high
        + data[1] = low
        + data[2] = close
+ output: np.ndarray of shape = (-1,) or pd.Series


#### KDJ
+ input: np.ndarray with shape = (3, -1)
    + data = (high, low, close) price:
        + data[0] = high
        + data[1] = low
        + data[2] = close
+ output: tuple[np.ndarray, np.ndarray, np.ndarray] or tuple[pd.Series, pd.Series, pd.Series]
    + 3 series of K, D, J (KDJ indicator)
    + shape of output: (3, -1)

#### STCK
+ input: np.ndarray with shape = (3, -1)
    + data = (high, low, close) price:
        + data[0] = high
        + data[1] = low
        + data[2] = close
+ output: np.ndarray of shape = (-1,) or pd.Series

#### STCD
+ input: np.ndarray with shape = (-1,) or pd.Series
    + data = (STCK) data
+ output: np.ndarray with shape = (-1,) or pd.Series

#### LWR
+ input: np.ndarray with shape = (3, -1)
    + data = (high, low, close) price:
        + data[0] = high
        + data[1] = low
        + data[2] = close
+ output: np.ndarray of shape = (-1,) or pd.Series

#### ADO
+ input: np.ndarray with shape = (4, -1)
    + data = (high, low, close, volumn):
        + data[0] = high
        + data[1] = low
        + data[2] = close
        + data[3] = volumn
+ output: np.ndarray of shape = (-1,) or pd.Series

#### CCI
+ input: np.ndarray with shape = (3, -1)
    + data = (high, low, close) price :
        + data[0] = high
        + data[1] = low
        + data[2] = close
+ output: np.ndarray of shape = (-1,) or pd.Series



### Note
+ np.ndarray with shape (-1,) is similar to pd.Series

