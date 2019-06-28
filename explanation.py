#This file has nothing to do with the app, it is just meant for explanation of the concepts

import pandas as pd #impoting pandas with name pd
import numpy as np #importing numpy with name np
import matplotlib.pyplot as plt #Using matplotlib's pyplot
df=pd.read_csv('lagged.csv') #reading the csv file
df=df.dropna() #dropping the null values
df=df.drop(['datetime_utc'],axis=1) #dropping the dates
df=df.drop(['Unnamed: 0',' _dewptm',' _fog',' _hail',' _hum',' _pressurem',' _snow',' _rain',' _thunder',' _tornado',' _wdird'],axis=1) #dropping current day columns
df1=pd.read_csv('lagged.csv') #reading csv again with a new variable name
df1=df1.dropna() #dropping null columns again
df1=df1.drop(['datetime_utc'],axis=1) #dropping date column
df1=df1.drop(['Unnamed: 0',' _dewptm',' _fog',' _hail',' _hum',' _pressurem',' _snow',' _tempm',' _thunder',' _tornado',' _wdird'],axis=1) #dropping current day columns
from sklearn.model_selection import train_test_split #importing train test split to use it for splitting of data
from sklearn.linear_model import LinearRegression #importing sklearn's linear regression
from sklearn.linear_model import LogisticRegression #importing sklearn's logistic regression for rain prediction
X_train,X_test,y_train,y_test=train_test_split(df.drop([' _tempm'],axis=1),df[' _tempm'],test_size=0.20) #Splitting train and test data in 80-20 parts
X_train1, X_test1, y_train1, y_test1 = train_test_split(df1.drop([' _rain'],axis=1),df1[' _rain'], test_size=0.20) #Splitting train and test again
regression_model = LinearRegression() #Making temperature model
regression_model.fit(X_train, y_train) #Fitting the datasets in the model
y_temp = regression_model.predict(X_train) #Predicting and Storing the outcome
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=200000).fit(X_train1, y_train1) #Making rain prediction model
y_rain=clf.predict(X_train1) #Storing the rain prediction model
from sklearn.externals import joblib #importing joblib library for dumping the model in pickle format
joblib.dump(clf, 'rain_model.pkl') #dumping rain model
joblib.dump(regression_model, 'temp_model.pkl') #dumping temp model

#Note that joblib version i.e sklearn version ust be constant if working on different machines otherwise the results may vary drastically
