import pandas as pd
import preprocess

performance = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/test/test_performance.csv")
performance = preprocess.manage_current(performance)
# print('PERFORMANCE;')
# print(performance)

demograficos = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/test/test_datos_demograficos.csv",
                            parse_dates=['birthdate'])
demograficos = preprocess.manage_demograficos(demograficos)
# print('DEMOGRAFICOS')
# print(demograficos)

demo_perf = demograficos.merge(performance, on="customerid", how="inner")
# print('DEMO_PERF')
# print(demo_perf)

previous = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/test/test_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'])
previous = preprocess.manage_previous(previous)
# print('PREVIOUS')
# print(previous)

merged = demo_perf.merge(previous, on="customerid", how="left")
# print('MERGED')
# print(merged)

merged.to_csv(r"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\merged_data\test\merged_test.csv",sep=';',index=False)
