'''
Parses the tags from Posts.xml
'''

import re
import sys

from lxml import etree
from dateutil import parser
from sqlalchemy.exc import IntegrityError

from data import Users, Questions, Answers, Tags, Session

def get_tags(s, post_object):
	return re.findall("\<(.*?)\>", post_object.get('Tags'))


def parse_xml_file(xml_file, tags_file):
	all_tags = set()
	with open(xml_file,'r') as f:
		for index, line in enumerate(f):
			line = line.strip()
			if line.startswith("<row"):
				node = etree.fromstring(line)
				post_object = node.attrib

				if post_object.get('PostTypeId') == "1":
					all_tags |= set(get_tags(s, post_object))
			if index % 10000 == 0:
				print index, "processed."
				sys.stdout.flush()
	print "Processed all lines:", len(all_tags)
	with open(tags_file, "w") as f:
		for tag in all_tags:
			print>>f, tag
	return all_tags


def insert_tags(all_tags):
	s = Session()
	for tag in all_tags:
		t = Tags(name=tag)
		try:
			s.add(t)
			s.commit()
			print "Added:", tag
		except IntegrityError as e:
			s.rollback()
			pass


if __name__=="__main__":
	#tags = parse_xml_file(sys.argv[1], sys.argv[2])
	with open(sys.argv[2]) as f:
		insert_tags([x.strip() for x in f])

