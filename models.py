import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('lagged.csv')
df=df.dropna()
df=df.drop(['datetime_utc'],axis=1)
df=df.drop(['Unnamed: 0',' _dewptm',' _fog',' _hail',' _hum',' _pressurem',' _snow',' _rain',' _thunder',' _tornado',' _wdird'],axis=1)
df1=pd.read_csv('lagged.csv')
df1=df1.dropna()
df1=df1.drop(['datetime_utc'],axis=1)
df1=df1.drop(['Unnamed: 0',' _dewptm',' _fog',' _hail',' _hum',' _pressurem',' _snow',' _tempm',' _thunder',' _tornado',' _wdird'],axis=1)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
X_train,X_test,y_train,y_test=train_test_split(df.drop([' _tempm'],axis=1),df[' _tempm'],test_size=0.20)
X_train1, X_test1, y_train1, y_test1 = train_test_split(df1.drop([' _rain'],axis=1),df1[' _rain'], test_size=0.20)
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
y_temp = regression_model.predict(X_train)
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=200000).fit(X_train1, y_train1)
y_rain=clf.predict(X_train1)
from sklearn.externals import joblib
joblib.dump(clf, 'rain_model.pkl')
joblib.dump(regression_model, 'temp_model.pkl')