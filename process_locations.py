from lxml import etree
import sqlite3
from sqlalchemy.sql import select,distinct
from sqlalchemy import (update, insert, and_)
import parser
from data import Location, Session, Users

session = Session()

def insert_users(Id, Reputation, Location, Views, UpVotes, DownVotes, Age):
	session.execute(insert(Users).values(Id = Id, Reputation = Reputation, Location= Location, Views= Views, UpVotes = UpVotes, DownVotes = DownVotes, Age = Age))
	session.commit()
	return "User information successfully inserted"

def get_unique_locations():
	locations=[]
	result = session.query(distinct(Users.Location)).all()
	return [x[0] for x in result]

def insert_locations():
	locations = get_unique_locations()
	for i, location in enumerate(locations):
		if session.query(Location).filter(Location.location == location).count():
			print i, location, "is already cached."
			continue
		location_params = parser.get_location_params(location)
		record = Location(**location_params)
		session.add(record)
		print i, location
		session.commit()
	session.commit()
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
					user_object[key] = node.attrib[key]
				users = data.Users(user_object.get('Id'),user_object.get('Reputation'),user_object.get('Location'),user_object.get('Views'),user_object.get('UpVotes'),user_object.get('DownVotes'),user_object.get('Age'))
				session = data.Session()
				session.add(users)
				session.commit()
				field_counter += 1
				print field_counter
				user_object = {}

if __name__=="__main__":
	print insert_locations()
