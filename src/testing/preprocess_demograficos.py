from datetime import datetime
import numpy as np
import pandas as pd

today = datetime.today()
pd.set_option('display.width', None)


def manage_demograficos(demograficos):
    demograficos['edad'] = demograficos['birthdate'].apply(
        lambda x: today.year - x.year -
                  ((today.month, today.day) < (x.month, x.day)))
    del demograficos['birthdate']
    demograficos.replace(np.nan, "UNKNOWN",inplace=True)
    categorical_cols = ['bank_account_type', 'bank_name_clients', 'bank_branch_clients', 'employment_status_clients','level_of_education_clients']
    return pd.get_dummies(demograficos, columns=categorical_cols)
#
#
# demograficos = pd.read_csv(r"C:\Users\Cristian\Documents\repos\G6_DP3\data\raw_data\train\train_datos_demograficos.csv",
#                            parse_dates=['birthdate'])
# manage_demograficos(demograficos)
