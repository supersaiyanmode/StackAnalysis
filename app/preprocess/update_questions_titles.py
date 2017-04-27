'''
Updates the title for table 'questions' 
'''

import re
import sys

from lxml import etree
from models.data import Session
 
def update_title(s, post_object, g):
	title = post_object.get('Title').replace("'","''").encode('utf-8')
	postid = post_object.get('Id')
	s = "UPDATE questions SET title = '" + title + "' WHERE id =" + postid+ ";\n"
	print>>g, s

def parse_lines(f, g):
	s = Session()
	for index, line in enumerate(f):
		line = line.strip()
		if line.startswith("<row"):
			node = etree.fromstring(line)
			post_object = node.attrib
			
			if post_object.get('PostTypeId') == "1":
				update_title(s, post_object, g)


if __name__=="__main__":
	with open(sys.argv[1], "r") as f, open(sys.argv[2], "w") as g: 
		parse_lines(f, g)
