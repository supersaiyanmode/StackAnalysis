import data
import parser
from lxml import etree
import sqlite3
from sqlalchemy.sql import select,distinct
from sqlalchemy import (update, insert, and_)

Session=data.Session()

def insert_users(Id, Reputation, Location, Views, UpVotes, DownVotes, Age):
    Session.execute(insert(Users).values(Id = Id, Reputation = Reputation, Location= Location, Views= Views, UpVotes = UpVotes, DownVotes = DownVotes, Age = Age))
    Session.commit()
    return "User information successfully inserted"

def get_unique_locations():
	locations=[]
	s = Session.query(distinct(data.Users.Location))	
	for row in s:
		locations.append(row)
	return list(set(locations))

def insert_locations():
	locations = get_unique_locations()
	count = 0
	for location in locations:
		i = insert(data.Location).values(parser.get_location_params(location))
		Session.execute(i)
		count+=1
		Session.commit()
		print count
	return "success"

def parse_xml_file(xml_file):
    list_of_fields = []
    user_object = {}
    field_counter = 0
    with open(xml_file,'r') as f:
        for x in f:
            x = x.strip()
            if x.startswith("<row"):
                node = etree.fromstring(x)
                for key in node.keys():
                   # if (field_counter == 0):
                   #    list_of_fields.append(key)
                    user_object[key] = node.attrib[key]    
                #print " PRINTING THE RECORDS NOW "
                users = data.Users(user_object.get('Id'),user_object.get('Reputation'),user_object.get('Location'),user_object.get('Views'),user_object.get('UpVotes'),user_object.get('DownVotes'),user_object.get('Age'))
                session = data.Session()
                session.add(users)
                session.commit()
				#print user_object    
                field_counter += 1
                print field_counter
                user_object = {}

if __name__=="__main__":
	print insert_locations()	
