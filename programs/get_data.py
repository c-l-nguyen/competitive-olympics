#!/usr/bin/python3

####
## Import libraries
####
import requests, csv, sys, os
import olympics_func as of
from bs4 import BeautifulSoup



####
## Build out CSV file to write out to
####

# specify url and check that it is valid
quote_page = str(sys.argv[1])
if "https://www.olympic.org/" not in quote_page:
    print("This is not an Olympics web page!")
    sys.exit(0)

# build CSV filename
domain_length = len('https://www.olympic.org/')
csvname = quote_page[domain_length:].replace("/","-") + '.csv'

# delete CSV file if already existing
if os.path.isfile('../data/'+csvname):
    os.remove('../data/'+csvname)

# write out header row to CSV file
of.csv_write(csvname,"Participant","Country","Result","Notes","Location","Event_Year")



####
## Parse HTML page with BeautofulSoup and write out to CSV
####

# query the website and return html to the variable page
page = requests.get(quote_page)

# parse html using BeautifulSoup and store in variable soup
soup = BeautifulSoup(page.content,'html.parser')
soup = soup.find('section',attrs={'class':"table-box"}) # use first table-box only

# get total number of participants for loop counter by counting all names
total_participants = len(soup.find_all("strong",attrs={'class':"name"}))
num_participants=list(range(0,total_participants))

(location, year) = of.loc_year(quote_page)

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
    of.csv_write(csvname,name,country,result,notes,location,year)
