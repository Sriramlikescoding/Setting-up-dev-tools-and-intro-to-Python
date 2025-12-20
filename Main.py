import sqlite3
import pandas as pd
database = "database.sqlite"
conn = sqlite3.connect(database)
print('databse connected succesfully')

tables = pd.read_sql("""select name from sqlite_master where type = 'table'""", conn)
print("Tables have been printed.")
print(tables)


#Player_Match

Player_Data=pd.read_sql("""select * from Player_Match""", conn)
print("data in player_match table is")
print(Player_Data)
conn.close()