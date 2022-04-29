import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
pd.set_option("display.width",None)

df = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/merged_data/train/merged_train.csv",sep=';')
df.drop(["customerid"],axis=1,inplace=True)
str_cols = []
df[str_cols] = df[str_cols].apply(pd.to_numeric)
pd.to_numeric(s)
print(df)
X, y = df.drop(["good_bad_flag"],axis=1), df['good_bad_flag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

D_train = xgb.DMatrix(X_train, label=y_train)
D_test = xgb.DMatrix(X_test, label=y_test)

baseline_model = xgb.XGBClassifier()
baseline_model.fit(X_train, y_train)

y_pred = baseline_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)