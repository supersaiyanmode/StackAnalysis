import lxml
from lxml import etree
import sqlite3
from geopy import geocoders
import pytz
from datetime import datetime
import tzlocal

def create_etree(path):
	return etree.parse("out.xml")

def is_bad(element):
	keys = element.keys()
	required_tags= set(['Id' , 'Reputation' , 'Location' , 'Views'])
	return False if required_tags<set(keys) else True

def filter_bad(tree):
	for item in tree.iter():
		if len(item.keys())!=0 and is_bad(item):
			item.getparent().remove(item)
	return tree
	
def get_latLong(place):
	g= geocoders.GoogleV3()
	result = g.geocode(place)
	if result is None:
		return None
	return result[1]

def get_timezone(cordinates):
	return geocoders.GoogleV3().timezone(cordinates)

def utc_to_local(timestamp , timezone):
	return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.utc).astimezone(timezone)

latlng = get_latLong('Chicago, IL')
if latlng is not None:
	print utc_to_local("2008-07-31T21:42:52.667", get_timezone(latlng))

#et = create_etree("out.xml")
#filtered_et = filter_bad(et)
#for item in filtered_et.iter():
#	print item.items()
#
#from lxml  import etree


#if __name__=="__main__":
    #parse_xml_file('out.xml')
