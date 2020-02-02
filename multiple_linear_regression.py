# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:34:51 2019

@author: hp
"""

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

dataset=pd.read_csv('50_Startups.csv');
x=dataset.iloc[:, :-1].values;
y=dataset.iloc[:, 4].values;

#We need to encode the categorical data...so encoding now*******
from sklearn.preprocessing import LabelEncoder,OneHotEncoder;
labelencoder_x=LabelEncoder();
x[:, 3]=labelencoder_x.fit_transform(x[:, 3]);

onehotencoder_x=OneHotEncoder(categorical_features=[3]);
x=onehotencoder_x.fit_transform(x).toarray();
#Avoiding the dummy variable trap*****
x=x[:, 1:];
#Splitting the dataset now*********
from sklearn.cross_validation import train_test_split;
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0);

#Applying the multiple linear regression model***
from sklearn.linear_model import LinearRegression;
regressor=LinearRegression();
regressor.fit(x_train,y_train);
#predicting the result*****
y_pred=regressor.predict(x_test);

#Now, optimizing the results using the backward elimination method******

import statsmodels.formula.api as sm;
x=np.append(arr=np.ones((50,1)).astype(int), values=x, axis=1);

x_opt=x[:,[0,1,2,3,4,5]];
regressor_OLS=sm.OLS(endog=y, exog=x_opt).fit();
regressor_OLS.summary()

x_opt=x[:,[0,1,3,4,5]];
regressor_OLS=sm.OLS(endog=y, exog=x_opt).fit();
regressor_OLS.summary()


x_opt=x[:,[0,3,4,5]];
regressor_OLS=sm.OLS(endog=y, exog=x_opt).fit();
regressor_OLS.summary()

x_opt=x[:,[0,3,5]];
regressor_OLS=sm.OLS(endog=y, exog=x_opt).fit();
regressor_OLS.summary()

x_opt=x[:,[0,3]];
regressor_OLS=sm.OLS(endog=y, exog=x_opt).fit();
regressor_OLS.summary()
#Splitting the dataset now*********
from sklearn.cross_validation import train_test_split;
x_train_opt, x_test_opt, y_train_opt, y_test_opt = train_test_split(x_opt, y, test_size=0.2, random_state=0);

regressor_opt=LinearRegression();
regressor_opt.fit(x_train_opt,y_train_opt);
y_pred_opt=regressor_opt.predict(x_test_opt);