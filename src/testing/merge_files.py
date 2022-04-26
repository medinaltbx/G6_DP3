import pandas as pd
import os
from functools import partial, reduce
import datetime
from dateutil.relativedelta import relativedelta
pd.set_option('display.width',None)
rdelta = relativedelta()

demograficos = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_datos_demograficos.csv")
performance = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_performance.csv")
demo_perf = demograficos.merge(performance, on="customerid", how="right")
# print(demo_perf)

previous = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'])
previous = previous.add_suffix("_prev")
# previous['Difference'] = (previous['firstrepaiddate_prev'] - previous['firstduedate_prev']).astype('timedelta64[h]')
previous['minutes_late'] = (previous.firstrepaiddate_prev - previous.firstduedate_prev) / pd.Timedelta(minutes=1)


print(previous)

# merged = demo_perf.merge(previous, left_on="customerid", right_on="customerid_prev", how="left")
# print(merged)


