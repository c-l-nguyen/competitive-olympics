#!/usr/bin/python3

####
## Import libraries
####
import sqlite3, glob, os
import pandas as pd



####
## Create SQL database and table to write data to
####

# remove combined data if already existing
if os.path.exists("../data/full_list_400m_mens.csv"):
    os.remove("../data/full_list_400m_mens.csv")

# set up sqlite db
connection = sqlite3.connect("../data/400m_mens.db")
cursor=connection.cursor()

# start out with fresh database table
cursor.execute("""DROP TABLE IF EXISTS full_400m_mens;""")

sql_command = """
CREATE TABLE full_400m_mens (  
participant VARCHAR(50),
country CHAR(3),
result VARCHAR(10),
notes VARCHAR(50),
location VARCHAR(25),
event_year INT
);
"""

cursor.execute(sql_command)



####
## Append all CSV data to table and output single, combined table as CSV
####

# get count and list of all CSVs and loop through to combine data into one table
csv_list = glob.glob('../data/*.csv')
csv_counter = len(csv_list)
csv_files = sorted(csv_list)

for i in range(csv_counter):
    csv_path = '../data/' + csv_files[i]
    df = pd.read_csv(csv_path)
    df.to_sql('full_400m_mens',connection,if_exists='append',index=False)

# write out full table to CSV file
df = pd.read_sql_query("SELECT * FROM full_400m_mens;", connection)
df.to_csv("../data/full_list_400m_mens.csv",encoding='utf-8',index=False)

connection.commit()

connection.close()
