import pandas as pd
import preprocess
from sklearn.preprocessing import OneHotEncoder

concat = pd.DataFrame()
encoder = None
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
    merged[str_cols] = merged[str_cols].apply(pd.to_numeric)


    # OneHot Encode cat variables
    # if set == "train":
    #     print("train")
    #     # categorical = ["bank_account_type","bank_name_clients","bank_branch_clients","employment_status_clients","level_of_education_clients"]
    #     # for c in categorical:
    #     #     encoder = OneHotEncoder()
    #     #     transformed = encoder.fit_transform(merged[[c]])
    #     #     array_hot_encoded = encoder.fit_transform(merged[categorical])
    #     #     data_hot_encoded = pd.DataFrame(array_hot_encoded)
    #     #     data_other_cols = merged.drop(columns=categorical)
    #     #     merged = pd.concat([data_hot_encoded, data_other_cols], axis=1)
    #     merged = preprocess.dummyEncode(merged, "train")
    #     exit(0)
    #
    # else:
    #     array_hot_encoded = encoder.transform(merged[categorical])
    #     data_hot_encoded = pd.DataFrame(array_hot_encoded, index=merged.index)
    #     data_other_cols = merged.drop(columns=categorical)
    #     merged = pd.concat([data_hot_encoded, data_other_cols], axis=1)


    concat = pd.concat([concat,merged],axis=0)

print(concat)
categorical = ["bank_account_type","bank_name_clients","bank_branch_clients","employment_status_clients","level_of_education_clients"]
concat = pd.get_dummies(concat, columns=categorical)

train, test =  concat[concat.good_bad_flag.notnull()], concat[~concat.good_bad_flag.notnull()].drop(['good_bad_flag'],axis=1)
train, test = train.fillna(0), test.fillna(0)

path = rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\input\merged_data\{set}\merged_{set}.csv"
train.to_csv(rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\input\merged_data\train\merged_train.csv",sep=';',index=False)
test.to_csv(rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\input\merged_data\test\merged_test.csv",sep=';',index=False)