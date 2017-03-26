import re
import sys

from lxml import etree
from dateutil import parser

from data import Users, Questions, Answers, Tags, Session

def get_tags(s, f):
	res = s.query(Tags.id, Tags.name).all()
	for item in res:
		print>> f, ('{} {}'.format(item[0], item[1]))

def update_poststags(tag_dict, g):
	with open(sys.argv[2], "r") as f:
		for line in f:
			line = line.strip()
			if line.startswith("<row"):
				node = etree.fromstring(line)
				post_object = node.attrib
				if post_object.get('PostTypeId') == "1":
					tags = re.findall("\<(.*?)\>", post_object.get('Tags'))
					for tag in tags:
						s = "INSERT INTO poststags(PostsId, TagsId) VALUES (" + \
							 post_object.get('Id') + "," + str(tag_dict[tag]) +");"
						print >> g, s
				
			
def tags_dict(path):
	tags = {}
	with open(path, "r") as f:
		for line in f:
			val= tuple(line.split())
			if val[1] not in tags:
				tags[val[1]]= int(val[0])
	return tags
          
if __name__=="__main__":
	s = Session()
#	with open(sys.argv[1], "w") as f:
#		get_tags(s, f)
	tags = tags_dict(sys.argv[1])
	with open(sys.argv[3], "w") as g:
		update_poststags(tags, g)
