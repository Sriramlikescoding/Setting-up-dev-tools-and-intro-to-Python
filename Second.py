#Create a table 
import pandas as pd
import sqlite3
connection = sqlite3.connect('Database.sqlite')
print('Database Connected Succesfully')
Tables = pd.read_sql_query("select Name from sqlite_master where type = 'table';", connection)
print("Tables in Database Opened")
print(Tables)
Player_Match = pd.read_sql_query("select * from Player_Match;", connection)
print("Plyaer Match data uus")
print(Player_Match)
print("First Five Rows of Table_Match is")
print(Player_Match.head())
null_PLayer_Match = pd.read_sql_query("select * from Player_Match where team_ID is null;", connection)
print("Null value in Player Match table is")
print(null_PLayer_Match)
#Match first five records
Match_Table = pd.read_sql_query("select * from Match;", connection)
print("First five rows of Match table is")
print(Match_Table.head())
connection.close()
print("Connection closed")
