'''
Simple models to train and test with
'''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from predict import predict

csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'

df = pd.read_csv(csv_path+f'2022\\2022_data.csv')
df = df.iloc[:,2:]

for year in [2016,2017,2018,2019,2021,2021]:
    small_df = pd.read_csv(csv_path+f'{year}\\{year}_data.csv')
    small_df = small_df.iloc[:,2:]
    df = pd.concat([df,small_df])

X = df.drop('Score_Dif',axis= 1) 
y = df['Score_Dif'] 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.2, random_state=101) 


#Linear Regression
model = LinearRegression() 
model.fit(X_train,y_train)
predictions = model.predict(X_test)
r_squared = model.score(X, y)

print( 
  'mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print( 
  'mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print(
    'R2: ', r_squared
) 

champion = predict('2023', model)
print(champion)