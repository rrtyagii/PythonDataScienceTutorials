import numpy as numpy 
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as seaborn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv("C:\\IIT\\Python Data Science\\Linear Regression With Python\\USA_Housing.csv")
print(df.describe())
seaborn.pairplot(df)
seaborn.distplot(df['Price'])
seaborn.heatmap(df.corr(), annot=True)

print()
df.drop('Address', axis=1, inplace=True)
print(df.info())

print(df.columns)
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


lrm = LinearRegression()
lrm.fit(X_train, y_train)
print(lrm.intercept_)
print(lrm.coef_)

print(X_train.columns)
cdf = pd.DataFrame(lrm.coef_, X.columns,columns =['Coeff'])
print(cdf)


Predictions from our test set
Predictions = lrm.predict(X_test)
pyplot.scatter(y_test, Predictions)

seaborn.distplot((y_test-Predictions))
print(metrics.mean_absolute_error(y_test, Predictions))

print(metrics.mean_squared_error(y_test, Predictions))

print(numpy.sqrt(metrics.mean_squared_error(y_test, Predictions)))








pyplot.show()