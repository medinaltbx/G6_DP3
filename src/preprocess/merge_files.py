import pandas as pd
import preprocess


set = "test"

performance = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/{set}/{set}_performance.csv")
performance = preprocess.manage_current(performance)
# print('PERFORMANCE;')
# print(performance)

demograficos = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/{set}/{set}_datos_demograficos.csv",
                            parse_dates=['birthdate'])
demograficos = preprocess.manage_demograficos(demograficos)
# print('DEMOGRAFICOS')
# print(demograficos)

demo_perf = demograficos.merge(performance, on="customerid", how="inner")
# print('DEMO_PERF')
# print(demo_perf)

previous = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/raw_data/{set}/{set}_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'])
previous = preprocess.manage_previous(previous)
# print('PREVIOUS')
# print(previous)

merged = demo_perf.merge(previous, on="customerid", how="left")
print('MERGED')
print(merged)

merged.drop(["longitude_gps", "latitude_gps"],axis=1,inplace=True)
str_cols = ["loanamount", "totaldue"]
# print(merged[str_cols].dtypes)
# # Remove decimals from string
# for c in str_cols:
#     print(merged[c])
#     merged[c] = merged[c].str.split(',').str[0]
merged[str_cols] = merged[str_cols].apply(pd.to_numeric)

merged.to_csv(rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\merged_data\{set}\merged_{set}.csv",sep=';',index=False)
