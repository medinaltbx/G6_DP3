import pandas as pd
from preprocess_previous_loan import manage_previous
pd.set_option('display.width',None)


demograficos = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_datos_demograficos.csv")
performance = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_performance.csv")
demo_perf = demograficos.merge(performance, on="customerid", how="right")
print(demo_perf)

previous = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'])
previous = manage_previous(previous)

print(previous)

# merged = demo_perf.merge(previous, left_on="customerid", right_on="customerid_prev", how="left")
# print(merged)


