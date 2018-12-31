# competitive_olympics
An extraction and analysis of competitive Olympic sports (currently only Men's 400m dash extracted and analyzed)

12/31/2018: Version 0.1 released
* Python web scraping program (get_data.py) now extracts first table from given Olympics URL
* Full CSV datasets included for Men's 400m dash as well as combined CSV dataset and SQLlite db
* Jupyter Notebook containing data analysis using pandas for Men's 400m dash included
* olympic_games.csv included as it was used to create commands for shell program
* Folder structure:
	- /programs contains Python programs and shell program to run
	- /data contains datasets
* Programs to be run as:
	1. runit.sh contains Python commands and inputs to run get_data.py
	2. get_data.py web scrapes the Olympics website to create CSV files and save in /data
	3. combine_data.py uses SQLlite and pandas to combine CSV files into one file for analysis