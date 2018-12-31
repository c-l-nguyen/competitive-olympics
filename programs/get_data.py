#!/usr/bin/python3

# import libraries
import requests, csv, sys
from bs4 import BeautifulSoup

# specify url
quote_page = str(sys.argv[1])

# special exception for Melborne/Stockholm 1956
if quote_page != "https://www.olympic.org/melbourne-/-stockholm-1956/athletics/400m-men":
	# split apart URL by delimiter and initialize location
	url_list=quote_page.split("/")
	location=""

	# parse location out of url_list
	venue=url_list[3].split("-")
	place=venue[:len(venue)-1]

	for i in range(len(place)):
		location+=(place[i]+" ")

	# format location and extract year of event
	location = location.rstrip().title()
	year=url_list[3].split("-")[-1]
else:
	location="Melbourne-Stockholm"
	year=1956

# build CSV filename
domain_length = len('https://www.olympic.org/')
csvname = quote_page[domain_length:].replace("/","-") + '.csv'

# write out header row to CSV file
with open('../data/'+ csvname,'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["Participant","Country","Result","Notes","Location","Event_Year"])

# query the website and return html to the variable page
page = requests.get(quote_page)

# parse html using BeautifulSoup and store in variable soup
soup = BeautifulSoup(page.content,'html.parser')
soup = soup.find('section',attrs={'class':"table-box"}) # use first table-box only

# get total number of participants for loop counter by counting all names
total_participants = len(soup.find_all("strong",attrs={'class':"name"}))
num_participants=list(range(0,total_participants))

for i in num_participants:
	name_box = soup.find_all("strong",attrs={"class":"name"})[i]
	name = name_box.text.title().strip()

	country_box = soup.find_all("div",attrs={"class":"profile-row"})[i]
	country = country_box.text.strip()

	result_box = soup.find_all("td",attrs={"class":"col3"})[i]
	result = result_box.text.strip()

	notes_box = soup.find_all("td",attrs={"class":"last mobile-hide"})[i]
	notes = notes_box.text.strip()


	# write out full results list to CSV file
	with open('../data/'+ csvname,'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name,country,result,notes, location, year]) # recall that location and year were parsed above
