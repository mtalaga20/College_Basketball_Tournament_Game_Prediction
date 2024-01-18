# College_Basketball_Tournament_Game_Prediction



Data is used from sports-reference.com

# Requirements
- Python 3.11.x version and packages listed in requirements.txt
- SQL Server and SSMS

# Getting Started
1. SQL Server Setup - This code base requires a SQL server database. You can change the names in the code, but I have named the database NCAAM_Stats.
2. The data is already pre-processed for training the model. To train a model, you can run run_model.py to save a .pkl file of a model. There are multiple models that can be used in a Voting Regressor, but gradient boost performed the best. Do this step before proceeding.
3. Task Scheduler Setup - Schedule the file named sportsreferencePipeline.py to be run daily to update the database. This will scrape data from sports-reference.com and pre-process it. It is set for the current season of 2024, which can be changed in the script.
4. Run the .NET web application to view and filter the data. Code is at https://github.com/mtalaga20/NCAAM_Web_App.

# Functionality
- 


### Bracket
W      -      S

E      -      MW

##Linear Correlation Results
### Positive Correlation
|Rank |Category|Score   | Calculation  |
|---|---|---|---|
| 1  | SRS -   | 0.56  |  Average point differentiala and strength of schedule |
| 2  | SOS - Strenth of Schedule  | 0.40  | |
| 3  | PPG  | 0.34  | |
| 4  | FG/G  | 0.28  | |
| 5  | W/L %  | 0.27  | |
| 6  | Coach Conference W/L %  | 0.26  | |
| 7  | Coach W/L %  | 0.24  | |
| 8  | Coach Sweet 16 App  | 0.24  | |
| 9  | Coach NCAA App  | 0.22  | |
| 10  | Efficient FG %  | 0.21  |(FG + 0.5 * 3P) / FGA |

### Negative Correlation
|Rank |Category|Score   | Calculation  |
|---|---|---|---|
| 1  | PACE - Number of possesions  | -0.11  | 40 * (Poss / (0.2 * Tm MP))  |
| 2  | FTr  | -0.10  | |
| 3  | TS% - True Shoot Percentage (with free throws) | -0.07  |PTS / (2 * (FGA + 0.475 * FTA)) |
