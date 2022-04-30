import pandas as pd
import preprocess


for set in ["train","test"]:
    performance = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/input/raw_data/{set}/{set}_performance.csv",decimal=",")
    performance = preprocess.manage_current(performance)
    # print('PERFORMANCE;')
    # print(performance)

    demograficos = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/input/raw_data/{set}/{set}_datos_demograficos.csv",
                                parse_dates=['birthdate'],decimal=".")
    demograficos = preprocess.manage_demograficos(demograficos)
    # print('DEMOGRAFICOS')
    # print(demograficos)

    demo_perf = demograficos.merge(performance, on="customerid", how="inner")
    # print('DEMO_PERF')
    # print(demo_perf)

    previous = pd.read_csv(rf"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/input/raw_data/{set}/{set}_previous_loan.csv",parse_dates=['firstduedate','firstrepaiddate'],decimal=".")
    previous = preprocess.manage_previous(previous)
    # print('PREVIOUS')
    # print(previous)

    merged = demo_perf.merge(previous, on="customerid", how="left")
    print('MERGED')
    print(merged)

    merged.drop(["longitude_gps", "latitude_gps"],axis=1,inplace=True)
    str_cols = ["loanamount", "totaldue"]
    print(merged[str_cols].dtypes)
    # Remove decimals from string
    # for c in str_cols:
    #     print(merged[c])
    #     merged[c] = merged[c].str.split(',').str[0]

    merged[str_cols] = merged[str_cols].apply(pd.to_numeric)
    with pd.option_context('display.max_rows', None):
        print(merged.dtypes)
    print(merged.dtypes)

    print(merged)
    path = rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\input\merged_data\{set}\merged_{set}.csv"
    print(path)
    merged.to_csv(path,sep=';',index=False)