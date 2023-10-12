'''
Not yet functional
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from predict import predict

csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'

df = pd.read_csv(csv_path+f'2022\\2022_data.csv')
df = df.iloc[:,2:]

for year in [2016,2017,2018,2019,2021]:
    small_df = pd.read_csv(csv_path+f'{year}\\{year}_data.csv')
    small_df = small_df.iloc[:,2:]
    df = pd.concat([df,small_df])

X = df.drop('Score_Dif',axis= 1) 
y = df['Score_Dif'].values
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.2, random_state=101) 

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape)

regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

results = predict('2023',regressor)
print(results)
'''