import pandas as pd
from preprocess_previous_loan import manage_previous
from preprocess_current_loan import manage_current
from preprocess_demograficos import manage_demograficos
pd.set_option('display.width',None)


performance = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_performance.csv")
performance = manage_current(performance)
print('PERFORMANCE;')
print(performance)

demograficos = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_datos_demograficos.csv",
                            parse_dates=['birthdate'])
demograficos = manage_demograficos(demograficos)
print('DEMOGRAFICOS')
print(demograficos)

demo_perf = demograficos.merge(performance, on="customerid", how="inner")
print('DEMO_PERF')
print(demo_perf)

previous = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'])
previous = manage_previous(previous)
print('PREVIOUS')
print(previous)

merged = demo_perf.merge(previous, on="customerid", how="left")
print('MERGED')
print(merged)


