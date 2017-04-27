'''
Creates 2-Itemsets from the and prints the tags and the frequency.
'''

import sys
import json
sys.path.insert(0, '..')

from models.data import session_factory as session


for line in sys.stdin:
	tag1, tag2 = map(int, line.strip().split())
	query1 = "select postsid from poststags where tagsid = " + str(tag1)
	query2 = "select postsid from poststags where tagsid = " + str(tag2)
	query = "select count(*) from (" + query1 + " intersect " + query2 + ") t"

	res = session.execute(query)
	print tag1, tag2, list(res)[0][0]
	sys.stdout.flush()

