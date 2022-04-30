import pandas as pd

merged = pd.read_csv(r"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\merged_data\test\merged_test.csv",sep=';')

with pd.option_context('display.max_rows', None):
    print(merged.dtypes)
