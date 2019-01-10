import csv

def loc_year(quote_page):
	""" Get the location and year of Olympic event from the URL """
	if quote_page == "https://www.olympic.org/melbourne-/-stockholm-1956/athletics/400m-men":
		location="Melbourne-Stockholm"
		year=1956
	else:
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

	return (location, year)

def csv_write(csvname,name,country,result,notes,location,year):
	""" Write out to CSV file """
	with open('../data/'+ csvname,'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name,country,result,notes,location,year])

	return