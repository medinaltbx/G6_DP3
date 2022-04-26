import pandas as pd
import os
from functools import partial, reduce

pd.set_option('display.width',None)

set = 'train'
path = rf"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\{set}"

dfs = []
for root,dirs,files in os.walk(path):
    for file in files:
        print(file)
        if file.endswith(".csv"):
            df = pd.read_csv(path+"/"+file)
            print(df)
            dfs.append(df)


df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['customerid'],
                                            how='right'), dfs)
print(df_merged)