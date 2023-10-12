'''
Part C
1. Take games and score result and combine differentials for two teams to form one differential
'''

import pandas as pd
import numpy as np

# -- PART C -- #
csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'
for year in [2016,2017,2018,2019,2021,2022,2023]:
    games = pd.read_csv(csv_path + f'{year}\\tourney_games.csv').to_numpy()
    basic_dif = pd.read_csv(csv_path + f'{year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{year}\\adv_differential.csv')
    column_size = len(basic_dif.columns)+len(adv_dif.columns)
    final_dif = np.empty(shape=[0,column_size-1])

    for i in range(games.shape[0]):
        away_team = games[i][0]
        home_team = games[i][1]
        score_differential = games[i][2] #Differential favors home team where it is (home points - away points)

        away_basic = basic_dif.loc[basic_dif['School'] == away_team].to_numpy().flatten()
        away_adv = adv_dif.loc[adv_dif['School'] == away_team].to_numpy().flatten()

        home_basic = basic_dif.loc[basic_dif['School'] == home_team].to_numpy().flatten()
        home_adv = adv_dif.loc[adv_dif['School'] == home_team].to_numpy().flatten()

        new_row = [away_team, home_team]
        for j in range(2, (column_size-2)):
            if j<len(basic_dif.columns):
                new_row.append(home_basic[j]-away_basic[j])
            else:
                new_row.append(home_adv[j-len(basic_dif.columns)+2] - away_adv[j-len(basic_dif.columns)+2])
                
        new_row.append(score_differential)
        final_dif = np.vstack((final_dif, np.array(new_row)))
        
    
    columns = ["Away","Home"]
    columns.extend(basic_dif.columns[2:])
    columns.extend(adv_dif.columns[2:])
    columns.append("Score_Dif")
    
    df = pd.DataFrame(final_dif, columns=columns)
    df.to_csv(csv_path + f'{year}\\{year}_data.csv', index=False)

        