'''
Contains the functions related to Google Geocoders.
'''

import lxml
import geocoder
import sqlite3
from geopy import geocoders
from geopy.exc import GeocoderParseError
import pytz
from datetime import datetime

def get_lat_long(place):
	g= geocoders.GoogleV3()
	result = g.geocode(place)
	if result is None:
		return None
	return result[1]

def get_timezone(cordinates):
	try:
		return geocoders.GoogleV3().timezone(cordinates).zone
	except GeocoderParseError:
		return None

def utc_to_local(timestamp , timezone):
	date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
	utc_date = pytz.utc.localize(date)
	return utc_date.astimezone(timezone)

def bounding_box(place):
	g = geocoders.google(place)
	return g.geojson['bbox']  #return [Left South Right North] cordinates

def get_location_params(location):
	g= geocoder.google(location)
	if not g.latlng:
		return {'location': location}
	timezone =  get_timezone(g.latlng)
	bbox = g.geojson['bbox']
	return {
		'location': location,
		'city': g.city,
		'state':g.state,
		'timezone': timezone,
		'country':g.country,
		'left':bbox[0],
		'bottom':bbox[1],
		'right':bbox[2],
		'top':bbox[3]
	}

#latlng = get_lat_long('chicago')
#if latlng is not None:
#	print utc_to_local("2008-07-31T21:42:52.667", get_timezone(latlng))
