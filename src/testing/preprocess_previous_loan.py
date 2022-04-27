import pandas as pd
pd.set_option('display.width',None)


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
    print(res)
    exit(0)
