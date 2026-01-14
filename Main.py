import pandas as p
import sqlite3
import numpy 
connection = sqlite3.connect("Database.sqlite")
tables = p.read_sql("""select * from sqlite_master where type = 'table'""", connection)
print(tables)
teams = p.read_sql("""select * from Match""", connection)
Match = p.read_sql("""select * from Team""", connection)
print(teams)
print(Match)
#Fetch details of all matches played by team, csk in 2015.
Details = p.read_sql("""select Match_ID, Team_2, Toss_Winner, Match_Winner from Match where Team_1 = (select Team_1 from Match where Team_1 == 3 and Season_ID == 8)""", connection)
print(Details)
#Fetch Details of all matches where batsman scores more than 5, in 2015
Details2 = p.read_sql("""select Match_ID, Runs_Scored, Innings_No from Batsman_Scored where Runs_Scored > 5 and Match_ID in (select Match_ID from Match where Season_ID == 8)""", connection)
print(Details2)
#Fetch Details of Matches played in 2015 where Total Runs Scored > Average Scored Runs 
Details3 = p.read_sql("""select Match_ID, Runs_Scored, Innings_No from Batsman_Scored where Innings_No ==1 and Runs_Scored > (select AVG(Runs_Scored) from Batsman_Scored)""", connection)
print(Details3)