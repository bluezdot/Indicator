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

from indicator import *
import pandas as pd
import matplotlib.pyplot as plt


def plot_ind(df, is_sma: bool, is_ema: bool, is_bband: bool, is_adx: bool, is_kdj, begin: int, end: int, save_to_image: str = "img.jpg"):
    ins_set = IndicatorSet()
    ins_set.insert_data_frame(df[begin:end], ["price_at_time"], timestamp_column="timestamp")

    # ins_set.insert_column(df["price_at_time"][:first], "price_at_time", False)
    # ins_set.insert_column(df["timestamp"][:first], "timestamp", True)
    
    ins_set.generate_ohlc("price_at_time", "15T")

    if is_sma:
        ins_set.insert_indicator(SMAIndicator(7), "sma7", ["close"], ["SMA 7"])
        ins_set.insert_indicator(SMAIndicator(25), "sma25", ["close"], ["SMA 25"])
        ins_set.insert_indicator(SMAIndicator(99), "sma99", ["close"], ["SMA 99"])

    if is_ema:
        ins_set.insert_indicator(EMAIndicator(7), "ema7", ["close"], ["EMA 7"])
        ins_set.insert_indicator(EMAIndicator(25), "ema25", ["close"], ["EMA 25"])
        ins_set.insert_indicator(EMAIndicator(99), "ema99", ["close"], ["EMA 99"])

    if is_bband:
        ins_set.insert_indicator(BBANDSIndicator(10), "bollingers", ["close"], ["bband upper", "bband middle", "bband lower"])

    if is_adx:
        ins_set.insert_indicator(ADXIndicator(14), "adx14", ["high", "low", "close"], ["ADX 14"])

    if is_adx:
        ins_set.insert_indicator(KDJIndicator(), "kdj", ["high", "low", "close"], ["K", "D", "J"])

    ins_set.calculate()

    num_ind = sum([is_sma, is_ema, is_bband, is_adx, is_kdj])
    if end is None:
        end = df.shape[0]

    fig = plt.figure(figsize=((end - begin) / 50, 3 * num_ind))
    axes = fig.subplots(num_ind, 1, sharex=True)

    if num_ind == 1:
        axes = [axes]

    num_ind = 0

    if is_sma:
        ins_set.plot(axes[num_ind], columns=["price_at_time"], names=["sma7", 'sma25', 'sma99'])
        num_ind += 1

    if is_ema:
        ins_set.plot(axes[num_ind], columns=["price_at_time"], names=["ema7", 'ema25', 'ema99'])
        num_ind += 1

    if is_bband:
        ins_set.plot(axes[num_ind], columns=["price_at_time"], names=['bollingers'])
        num_ind += 1

    if is_adx:
        ax = axes[num_ind]
        ins_set.plot(ax, names=["adx14"])
        ax.axhline(y = 50, color = 'r', linestyle = '-')
        ax.axhline(y = 25, color = 'r', linestyle = '-')
        num_ind += 1
        
    if is_kdj:
        # ins_set.plot(axes[num_ind], columns=["price_at_time"], names=['kdj'])
        ins_set.plot(axes[num_ind], names=['kdj'])
        num_ind += 1

    fig.tight_layout()
    fig.savefig(save_to_image)
    # plt.show()
    ins_set.to_csv("./data_/BNB-inds.csv")


df = pd.read_csv("./data_/BNBUSDT_3m_2022-01-01_2022-05-19.csv")
plot_ind(df, True, True, True, True, True, None, None)