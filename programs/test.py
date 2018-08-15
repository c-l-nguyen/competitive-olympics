# import libraries
import requests, csv
from bs4 import BeautifulSoup

# specify url
quote_page ='https://www.olympic.org/pyeongchang-2018/biathlon/mens-12-5km-pursuit'
#quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

# query the website and return html to the variable page
# urlopen present in urllib.request in Python 3
page = requests.get(quote_page)

# parse html using BeautifulSoup and store in variable soup
soup = BeautifulSoup(page.content,'html.parser')

# test BeautifulSoup html parser output
#name_box = soup.find("span",attrs={"class":"priceText__1853e8a5"})
#name = name_box.text
#print(name_box)

num_participants=list(range(0,60))

for i in num_participants:
	# Take out the <strong> of name and get its value
	name_box = soup.find_all("strong",attrs={"class":"name"})[61+i].text
	#print(name_box)

	country_box = soup.find_all("div",attrs={"class":"profile-row"})[0+i]
	country = country_box.text.strip()
	#print(country)

	result_box = soup.find_all("td",attrs={"class":"col3"})[0+i]
	result = result_box.text.strip()
	#print(result)

	# write out participant list to CSV file
	with open('pyeongchang-2018-biathlon-mens-12-5km-pursuit.csv','a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name_box,country,result])

