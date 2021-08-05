# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from numpy import mean
from numpy import std
from sklearn.linear_model import LinearRegression

df = pd.read_csv("regressiondata.csv")

# data_mean, data_std = mean(df), std(df)
# cut_off = data_std * 3
# lower, upper = data_mean - cut_off, data_mean + cut_off

# # Remove those 2 outliers.. 
# dfnew = df[df["Sqft"] <= upper[2]] # remove the sqft outlier
# dffinal =  dfnew[dfnew["Price"] <= upper[3]] # remove the price outlie

# price column for prediction
Y= df.iloc[:, -1]

# bed bath and sqft for predictors
X = df.iloc[:, 1:4]

regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, Y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[3,2,2000]]))