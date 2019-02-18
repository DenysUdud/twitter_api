# program 3 from lab 3 second semester
# the aim to make map with locations of users friends
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request
from geopy.geocoders import Nominatim
from mymodule import twurl
import pandas
import folium


def json_maker(acct):
	'''
	(str) -> dict
	This functions reads name of user in stdin and returns json
	object with information about typed users account.
	'''

	# https://apps.twitter.com/
	# Create App and get the four strings, put them in hidden.py

	TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	url = twurl.augment(TWITTER_URL,
						{'screen_name': acct, 'count': '100'})
	print('Retrieving', url)
	connection = urllib.request.urlopen(url, context=ctx, timeout=100000)
	data = connection.read().decode()

	# js json string

	js = json.loads(data)

	with open('twitterj.txt', "w") as f:
		json.dump(js, f, indent=2)

	headers = dict(connection.getheaders())
	print('Remaining', headers['x-rate-limit-remaining'])

	return js


def location_reader(js_dict):
	'''
	(dict) -> str

	This function gets  of typed users friends and makes
	csv file with latitude, logitude and names of people.
	Returns name of csv file
	'''
	geolocator = Nominatim(user_agent="specify_your_app_name_here",
						   timeout=50000)

	# with open('twitterj.txt', "r") as f:
	# 	js_dict = json.load(f)
	with open('loocations.csv', "w") as file:
		file.write('lat,lon,name\n')
		for user in js_dict['users']:
			try:
				location = geolocator.geocode(user['location'])
				line = "{},{},{}\n".format(str(location.latitude),
										   str(location.longitude),
										   user['name'])
			except AttributeError:
				if len(user['location']) < 1:
					continue
				else:
					location = geolocator.geocode(user['location'][-1])
					line = "{},{},{}\n".format(
						str(location.latitude),
						str(location.longitude),
						user['name'])


			file.write(line)
	return 'loocations.csv'


def map_maker(name_csv_file, account):
	'''
	(str, str) -> str
	This function makes the map of users friends locations.
	Firstly it reads csv file, then makes map and after this
	writes map to Map_(input_user)
	'''
	data = pandas.read_csv(name_csv_file)
	lat = data['lat']
	lon = data['lon']
	name = data['name']
	mappy = folium.Map()
	fg_simple = folium.FeatureGroup(name="Locations_map")
	for lt, ln, usern in zip(lat, lon, name):
		fg_simple.add_child(folium.Marker(location=[lt, ln],
										  popup=usern,
										  icon=folium.Icon()
										  )
							)
	mappy.add_child(fg_simple)
	file_name = "Map_{}.html".format(account)
	mappy.save(file_name)
	return file_name


if __name__ == "__main__":
	inp_detect = False
	while inp_detect == False:
		print('')
		acct = input('Enter Twitter Account:')
		if len(acct) > 1:
			inp_detect = True
	jsonfile = json_maker(acct)
	html_name = map_maker(location_reader(jsonfile), acct)
	print("Your file in {}".format(html_name))