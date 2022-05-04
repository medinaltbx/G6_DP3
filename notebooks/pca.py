#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:55:41 2022

@author: RicardoVReig
"""
import pandas as pd                    #gestionar dataframes
import numpy as np  
import seaborn as sns
import matplotlib 
from pandas_profiling import ProfileReport
import pathlib
import xgboost as xgb
from xgboost import XGBRegressor
from xgboost import plot_importance
from matplotlib import pyplot
import matplotlib.pyplot as plt
import ipywidgets
import sklearn
get_ipython().run_line_magic('matplotlib', 'inline')


dfpca = pd.read_csv(r"https://raw.githubusercontent.com/medinaltbx/G6_DP3/master/data/input/merged_data/train/merged_train.csv", sep=';' , decimal='.')
dfpca.head()
dfpca.dtypes

X = dfpca.drop('good_bad_flag', 1)
y = dfpca['good_bad_flag']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Standarization, avoiding customerid. good to use with gaussian distribution
from sklearn.preprocessing import StandardScaler
#We should try with normalization instead. good to use when you know that the distribution of your data does not follow a Gaussian distribution
sc = StandardScaler()
X_train = sc.fit_transform(X_train.loc[:, X_train.columns != 'customerid'])
X_test = sc.transform(X_test.loc[:, X_test.columns != 'customerid'])

#here I want to check wether mean tends to 0:
np.mean(X_test[5])
np.mean(X_train[1])

#PCA

from sklearn.decomposition import PCA

pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

#returns the variance caused by each of the principal components.
explained_variance = pca.explained_variance_ratio_


#1 principal component to train our algorithm:
pca = PCA(n_components=1)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

#0.79acc

#2 principal component to train our algorithm:
pca = PCA(n_components=2)
X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train2, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test2)


cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

#0.79 acc

#all features


pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

explained_variance = pca.explained_variance_ratio_


classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)


cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

#0.79acc
