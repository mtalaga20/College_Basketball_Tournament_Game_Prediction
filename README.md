# College_Basketball_Tournament_Game_Prediction



Data is used from sports-reference.com

# Getting Started
1. SQL Server Setup - This code base requires a SQL server database. You can change the names in the code, but I have named the database NCAAM_Stats.
2. The data is already pre-processed for training the model. To train a model, you can run run_model.py to save a .pkl file of a model. There are multiple models that can be used in a Voting Regressor, but gradient boost performed the best. Do this step before proceeding.
3. Task Scheduler Setup - Schedule the file named sportsreferencePipeline.py to be run daily to update the database. This will scrape data from sports-reference.com and pre-process it. It is set for the current season of 2024, which can be changed in the script.
4. Run the .NET web application to view and filter the data.


## Bracket
W      -      S

E      -      MW