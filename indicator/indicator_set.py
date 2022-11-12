import pandas as pd
import matplotlib.axis as axis
from .base_indicator import BaseIndicator


class LackTimestampException(Exception):
    pass


class IndicatorSet:
    def __init__(self) -> None:
        self.__df = pd.DataFrame()
        self.__indicators = dict()
        self.__input_columns = dict()
        self.__output_columns = dict()
        self.__timestamp_column = None

    def insert_data_frame(self, df: pd.DataFrame, columns: list = None, timestamp_column: str = None, timestamp_unit='s'):
        """
        Insert data to data frame df 
        `Timestamp` column must insert separately

        `WARINING:` data in column will be replaced if column name exists in data frame

        Parameters
        ----------
            df: pd.DataFrame
                Data frame
            columns: list[str], default is `None`
                List of tuple of column name, exclude timestamp column
                `WARINING:` data will be replaced if column name exists in data frame
            timestamp_column: str, default is `None`
                name of timestamp column
            timestamp_unit: str, default is `s`
                timestamp unit, can be `d`, `s`, `ms`, ...
        """
        self.__df = pd.DataFrame()

        for col_name in columns:
            self.insert_column(df[col_name], col_name, False)

        if timestamp_column is not None:
            self.insert_column(df[timestamp_column], timestamp_column, True, timestamp_unit)

    def insert_column(self, data, column_name: str, is_timestamps: bool, timestamp_unit='s'):
        """
        Insert column data to data frame df 

        `WARINING:` data will be replaced if `column_name` exists in data frame

        Parameters
        ----------
            data: list or array like
                Data of column
            column_name: str
                Name of column to insert
            is_timestamps: bool
                `True` if this column is timestamp column,
                Otherwise, `False`
            timestamp_unit: str, default is `s`
                timestamp unit, can be `d`, `s`, `ms`, ...
        """

        if is_timestamps:
            self.__timestamp_column = column_name
            self.__df[column_name] = pd.to_datetime(data, unit=timestamp_unit)            
            self.__df = self.__df.set_index(column_name)

        else:
            self.__df[column_name] = data

    def insert_indicator(self, indicator: BaseIndicator, name: str, input_columns: list, output_columns: list):
        """
        Insert indicator to indicator set

        Parameters
        ----------
            indicator: BaseIndicator
                Indicator to insert
            name: str
                Name of indicator, should not conflict
            input_columns: list
                List of columns used as input data for this indicator
            output_columns: list
                List of columns used to stored output data for this indicator
        """
        if self.__indicators.get(name) is not None:
            raise ValueError("Indicator with name '" + name + "' has been inserted")

        self.__indicators[name] = indicator
        
        if input_columns is None:
            input_columns = list()
        
        self.__input_columns[name] = input_columns
        self.__output_columns[name] = output_columns

    def remove_indicator(self, name: str):
        """
        Remove indicator from indicator set

        Parameters
        ----------
            name: str
                Name of indicator
        """
        if self.__indicators.get(name) is None:
            print("Not found indicator with name '" +
                  name + "' in indicator set")
        else:
            self.__indicators.pop(name)
            self.__input_columns.pop(name)
            self.__output_columns.pop(name)

    def generate_ohlc(self, column_name: str, period: str, join: str = "inner"):
        """
        Generate open, high, low, close data

        You cannot generate ohlc data for more than `one` column
        If you do, previous data will be overwritten

        You have to input timestamp data before generate ohlc data

        After generate ohlc data, the ohlc data will be concatenated to current data frame
            some timestamp will be missed bases on how you `join` the ohlc data 
            after the data frame is resampled

        Parameters
        ----------
            column_name: str
                Name of column used to generate data
            period: str
                Time period to resample data

                `period` has the format: a number next to a word,
                For example: `period = "2T"` mean time period is 2 minute,

                We have some common time period:
                    `M`: month
                    `W`: week
                    `D`: day
                    `H`: hour
                    `T` or `min`: minute
                    `S` second
                    `L` or `ms`: millisecond 
                    `U` or `us`: microsecond
                    `N`: nanosecond
                See pandas.Series.resample() for more information
            join: str, default is `inner`
                Method to join generated data
                See pandas.concat() for more information
        """
        if self.__timestamp_column is None:
            raise ValueError("You must insert timestamp data before generate ohlc data")

        self.__df = pd.concat([self.__df, self.__df[column_name].resample(period).ohlc()], axis=1, join=join)

    def __get_input(self, input_columns: list):
        if len(input_columns) == 1:
            return self.__df[input_columns[0]]
        
        return [self.__df[col] for col in input_columns]

    def calculate(self):
        """
        for example if sma is calculated but ema is not => how to detect that
        """
        for name, indicator in self.__indicators.items():
            input_cols = self.__input_columns[name]
            output_cols = self.__output_columns[name]

            result = indicator.calculate(self.__get_input(input_cols))

            if len(output_cols) > 1:
                for col, res in zip(output_cols, result):
                    self.__df[col] = res
            else:
                self.__df[output_cols[0]] = result

    def plot(self, ax: axis.Axis, names: list = None, exclude_names: list=None, columns: list = None):
        """
        Show the plot of indication in the list of names. Show all if names is None

        Parameters
        ----------
            ax: axis.Axis
                Axis of matplotlib for ploting
            names: list, default is `None`
                List of names to plot
            exclude_names: list, default is None
                `exclude_names` has higher order than `names`
            columns: list, default is `None`
                List of column names to plot data
        """

        if columns is not None:
            for col in columns:
                ax.plot(self.__df[col], label=col)

        if names is None:
            names = list(self.__indicators.keys())
        
        if exclude_names is not None:
            for name in exclude_names:
                names.remove(name)

        for name in names:
            if self.__indicators.get(name) is None:
                continue

            for col in self.__output_columns[name]:
                ax.plot(self.__df[col], label=col)
        
        ax.legend(loc='upper left')
    
    def to_csv(self, file_path: str):
        """
        Export object to a comma-separated values (csv) file.

        Parameters
        ----------
            file_path: str
                Path of input file
        """
        self.__df.to_csv(file_path)

    @property
    def df(self):
        return self.__df