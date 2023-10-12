'''
Simple models to train and test with
'''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 

from sklearn.metrics import mean_squared_error, mean_absolute_error 
import keras
from keras.models import Sequential
from keras.layers import Dense
from predict import predict

#from utility import generate_mock_games

csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'

df = pd.read_csv(csv_path+f'2022\\2022_data.csv')
df = df.iloc[:,2:]

for year in [2016,2017,2018,2019,2021]:
    small_df = pd.read_csv(csv_path+f'{year}\\{year}_data.csv')
    small_df = small_df.iloc[:,2:]
    df = pd.concat([df,small_df])

X = df.drop('Score_Dif',axis= 1) 
Y = df['Score_Dif'] 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=40)


#Train
input_size = len(df.columns)-1
model = Sequential()
model.add(Dense(500, input_dim=input_size, activation= "relu"))
model.add(Dense(100, activation= "relu"))
model.add(Dense(50, activation= "relu"))
model.add(Dense(1))

model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])
model.fit(X_train, y_train, epochs=16)

pred_test = model.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,pred_test)))

champion = predict('2023', model)
print(champion)
