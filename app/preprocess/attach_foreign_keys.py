'''
Updates the referential fields in tables 'questions' and 'answers' 
'''

import re
import sys
from itertools import islice

from lxml import etree
from dateutil import parser


def attach_question(post_object, all_answers):
	if "AcceptedAnswerId" in post_object:
		val = int(post_object["AcceptedAnswerId"])
		if val in all_answers:
			s = "UPDATE questions SET accepted_answer_id = " + str(val)
			s += " WHERE questions.id = " + str(post_object["Id"])
			return s

def attach_answer(post_object):
	return "UPDATE answers SET question_id = " + str(post_object["ParentId"]) +\
					" WHERE answers.id = " + str(post_object["Id"])


def attach_foreignkeys(ans_file, gen, g):
	all_answers = {int(x.strip()) for x in open(ans_file)}
	print "Answers loaded."

	for index, line in enumerate(gen):
		line = line.strip()
		if line.startswith("<row"):
			node = etree.fromstring(line)
			post_object = node.attrib

			if post_object.get('PostTypeId') == "1":
				res = attach_question(post_object, all_answers)
				if res is not None:
					print>>g, res
			elif post_object.get('PostTypeId') == "2":
				res = attach_answer(post_object)
				if res is not None:
					print>>g, res
		if index % 2000 == 0:
			print index, "attached."
			sys.stdout.flush()


if __name__=="__main__":
	with open(sys.argv[1]) as f, open(sys.argv[2], "w") as g:
		gen = islice(f, int(sys.argv[3]), int(sys.argv[4]))
		attach_foreignkeys(sys.argv[5], gen, g)

