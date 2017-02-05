import lxml
from lxml import etree
import sqlite3
from geopy import geocoders

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
	place, (lat, lng)=g.geocode(place)
	return (lat, lng)

def get_timezone(cordinates):
	return geocoders.GoogleV3().timezone(cordinates)

print get_timezone(get_latLong('India'))
def parse_xml_file(xml_file):
    with open(xml_file,'r') as f:
        for x in f:
            x = x.strip()
            if x.startswith("<row"):
                node = etree.fromstring(x)
                for key in node.keys():
                    print "key = "+key+" " +node.attrib[key],

#et = create_etree("out.xml")
#filtered_et = filter_bad(et)
#for item in filtered_et.iter():
#	print item.items()
#
#from lxml  import etree


#if __name__=="__main__":
    #parse_xml_file('out.xml')
