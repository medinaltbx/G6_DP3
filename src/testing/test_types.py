import glob, os
import pandas as pd

for set in ["train","test"]:
    directory_path = rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\input\raw_data\{set}"
    csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

    for f in csv_files:
        x = pd.read_csv(f, sep=',')
        print(f, x.shape)
