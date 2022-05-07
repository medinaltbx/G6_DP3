import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pickle

def manage_current(current):
    current.replace({'good_bad_flag': {'Good': 1, 'Bad': 0}},inplace=True)
    current.drop(['systemloanid','approveddate','creationdate'],axis=1,inplace=True)
    current['referredby'] = [1 if isinstance(s, str) else 0 for s in current['referredby']]
    return current

today = datetime.today()
pd.set_option('display.width', None)

def manage_demograficos(demograficos):
    demograficos['edad'] = demograficos['birthdate'].apply(
        lambda x: today.year - x.year -
                  ((today.month, today.day) < (x.month, x.day)))
    del demograficos['birthdate']
    demograficos.replace(np.nan, "UNKNOWN",inplace=True)
    categorical_cols = ['bank_account_type', 'bank_name_clients', 'bank_branch_clients', 'employment_status_clients','level_of_education_clients']
    # return pd.get_dummies(demograficos, columns=categorical_cols)
    return demograficos

def get_values(df):
    times_loaned = len(df)
    times_late = len(df[df['is_late'] == 1])
    times_referred = len(df.dropna())
    return times_loaned, times_late, times_referred


def manage_previous(previous):
    # Greater than 0 if not ok, negative if  ok
    previous['minutes_late'] = (previous.firstrepaiddate - previous.firstduedate) / pd.Timedelta(minutes=1)
    previous['is_late'] = [0 if x < 0 else 1 for x in previous.minutes_late]

    res = previous.groupby("customerid").apply(get_values).reset_index()
    res['times_loaned'], res['times_late'], res['times_referred'] = zip(*res[0])
    del res[0]
    return res

def dummyEncode(df, set):
    if set == "train":
        dc = {}
        columnsToEncode = ["bank_account_type","bank_name_clients","bank_branch_clients","employment_status_clients","level_of_education_clients"]
        for feature in columnsToEncode:
            try:
                print('DETNTRO DEL TRY')
                ohe = OneHotEncoder()
                print(ohe)
                print(df[feature])
                df = ohe.fit_transform(df[feature])
                print(df)
                exit(0)
                dc[feature] = ohe
            except:
                print('Error encoding ' + feature)

        with open(rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\encoder\encoding_dc.pkl", "wb") as file:
            pickle.dump(dc, file)
        return df

    else:
        dc = pickle.load(open(rf"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\encoder\encoding_dc.pkl", "wb"))
        print(dc)