#!/usr/bin/python3

# import libraries
import requests, csv, sys
from bs4 import BeautifulSoup

# specify url
quote_page = str(sys.argv[1])

# build CSV filename
domain_length = len('https://www.olympic.org/')
csvname = quote_page[domain_length:].replace("/","-") + '.csv'

# write out header row to CSV file
with open('../data/'+ csvname,'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["Participant","Country","Result","Notes"])

# query the website and return html to the variable page
page = requests.get(quote_page)

# parse html using BeautifulSoup and store in variable soup
soup = BeautifulSoup(page.content,'html.parser')

# get total number of participants for loop counter
total = soup.find_all("span",attrs={'class':"num-txt"})[-1]
total_participants = total.text.strip().replace(".","")
total_participants = int(total_participants)

num_participants=list(range(0,total_participants))

for i in num_participants:
	name_box = soup.find_all("strong",attrs={"class":"name"})[61+i]
	name = name_box.text.title().strip()
	#print(name)

	country_box = soup.find_all("div",attrs={"class":"profile-row"})[0+i]
	country = country_box.text.strip()
	#print(country)

	result_box = soup.find_all("td",attrs={"class":"col3"})[0+i]
	result = result_box.text.strip()
	#print(result)

	notes_box = soup.find_all("td",attrs={"class":"last mobile-hide"})[0+i]
	notes = notes_box.text.strip()
	#print(notes)

	#write out full results list to CSV file
	with open('../data/'+ csvname,'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name,country,result,notes])
