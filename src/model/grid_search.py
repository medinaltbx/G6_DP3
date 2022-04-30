import pandas as pd
from numpy.ma.bench import timer
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import accuracy_score
import xgboost as xgb
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
import pickle

pd.set_option("display.width",None)


df = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/input/merged_data/train/merged_train.csv",sep=';')
df.drop(["customerid"],axis=1,inplace=True)
X, y = df.drop(["good_bad_flag"],axis=1), df['good_bad_flag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


space={'max_depth': hp.quniform("max_depth", 3, 18, 1),
        'gamma': hp.uniform ('gamma', 1,9),
        'reg_alpha' : hp.quniform('reg_alpha', 40,180,1),
        'reg_lambda' : hp.uniform('reg_lambda', 0,1),
        'colsample_bytree' : hp.uniform('colsample_bytree', 0.5,1),
        'min_child_weight' : hp.quniform('min_child_weight', 0, 10, 1),
        'n_estimators': hp.choice("n_estimators", [100, 200, 300, 400,500]),
        'seed': 0
    }


def objective(space):
    clf = xgb.XGBClassifier(
        n_estimators=space['n_estimators'], max_depth=int(space['max_depth']), gamma=space['gamma'],
        reg_alpha=int(space['reg_alpha']), min_child_weight=int(space['min_child_weight']),
        colsample_bytree=int(space['colsample_bytree']))

    evaluation = [(X_train, y_train), (X_test, y_test)]

    clf.fit(X_train, y_train,
            eval_set=evaluation, eval_metric="auc",
            early_stopping_rounds=10, verbose=False)

    pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, pred > 0.5)
    print("SCORE:", accuracy)
    return {'loss': -accuracy, 'status': STATUS_OK}

trials = Trials()

best_hyperparams = fmin(fn = objective,
                        space = space,
                        algo = tpe.suggest,
                        max_evals = 100,
                        trials = trials)

print("The best hyperparameters are : ","\n")
print(best_hyperparams)

with open(r"C:\Users\Cristian Medina\Documents\EDEM\G6_DP3\data\hp\all_variables_best_hp.pkl","wb") as file:
    pickle.dump(best_hyperparams, file)