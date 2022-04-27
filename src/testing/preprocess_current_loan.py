import pandas as pd
pd.set_option('display.width',None)

def manage_current(current):
    current.replace({'good_bad_flag': {'Good': 1, 'Bad': 0}},inplace=True)
    current.drop(['systemloanid','approveddate','creationdate'],axis=1,inplace=True)
    current['referredby'] = [1 if isinstance(s, str) else 0 for s in current['referredby']]
    return current

