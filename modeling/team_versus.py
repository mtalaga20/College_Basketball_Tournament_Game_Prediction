import sys
import pickle
import math
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

try:
    csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'
    year = 2024 #TODO:
    team_one = sys.argv[1]
    team_two = sys.argv[2]
    
    basic_dif = pd.read_csv(csv_path + f'{year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{year}\\adv_differential.csv')
    coach = pd.read_csv(csv_path+f'{year}\\coach.csv')
    column_size = len(basic_dif.columns)+len(adv_dif.columns)

    with open(r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\modeling\best-model.pkl', 'rb') as f:
        model = pickle.load(f)

    for i in range(2):
        if i == 1:
            team_one = sys.argv[2]
            team_two = sys.argv[1]

        away_basic = basic_dif.loc[basic_dif['School'] == team_one].to_numpy().flatten()
        away_adv = adv_dif.loc[adv_dif['School'] == team_one].to_numpy().flatten()
        away_coach = coach.loc[coach['School'] == team_one].to_numpy().flatten()
        home_basic = basic_dif.loc[basic_dif['School'] == team_two].to_numpy().flatten()
        home_adv = adv_dif.loc[adv_dif['School'] == team_two].to_numpy().flatten()
        home_coach = coach.loc[coach['School'] == team_two].to_numpy().flatten()

        new_row = []
            #new_row = [away_team, home_team]
        for z in range(2, (column_size-2)):
            if z<len(basic_dif.columns):
                new_row.append(home_basic[z]-away_basic[z])
            else:
                new_row.append(home_adv[z-len(basic_dif.columns)+2] - away_adv[z-len(basic_dif.columns)+2])

        #Coach stats
        new_row.append(home_coach[14]-away_coach[14])
        new_row.append(home_coach[15]-away_coach[15])
        new_row.append(home_coach[16]-away_coach[16])
        new_row.append(home_coach[17]-away_coach[17])
        new_row.append(home_coach[18]-away_coach[18])
        new_row.append(home_coach[22]-away_coach[22])
        new_row.append(home_coach[23]-away_coach[23])
        new_row.append(home_coach[24]-away_coach[24])
        new_row.append(home_coach[25]-away_coach[25])
        new_row.append(0 if (math.isnan(home_coach[26]) or math.isnan(away_coach[26])) else int(home_coach[26])-int(away_coach[26]))

        new_row = [0 if math.isnan(i) else i for i in new_row] 

        if i == 0:
            pred = model.predict([new_row])[0]
        else:
            pred += model.predict([new_row])[0] * -1
            pred = pred / 2
    
    print(f'{team_one if pred > 0 else team_two} wins by {round(abs(pred) * 2) / 2}')

except Exception as e:
    print(e)