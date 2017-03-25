import re
import sys
from itertools import islice

from lxml import etree
from dateutil import parser

from data import Users, Questions, Answers, Tags, Session

def process_questions(s, post_object):
	mappings = {
		'Id': "id",
		'CreationDate': "creation_date",
		'Score': 'score',
		'OwnerUserId': 'author_id',
		'LastActivityDate': 'modified_date',
		'AnswerCount': "answer_count"
	}
	params = {y: post_object.get(x) for x, y in mappings.items()}
	params['creation_date'] = parser.parse(params['creation_date'])
	params['modified_date'] = parser.parse(params['modified_date'])
	question = Questions(**params)
	s.add(question)

def process_answers(s, post_object):
	mappings = {
		'Id': "id",
		'Score': 'score',
		'OwnerUserId': 'author_id',
		'CreationDate': "creation_date",
		'LastActivityDate': 'modified_date',
	}
	params = {y: post_object.get(x) for x, y in mappings.items()}
	params['creation_date'] = parser.parse(params['creation_date'])
	params['modified_date'] = parser.parse(params['modified_date'])
	answers = Answers(**params)
	s.add(answers)

def attach_question(s, post_object):
	question = s.query(Questions).get(int(post_object["Id"]))
	if "AcceptedAnswerId" in post_object:
		question.accepted_answer_id = int(post_object["AcceptedAnswerId"])
		s.add(question)

def attach_answer(s, post_object):
	answer = s.query(Answers).get(int(post_object["Id"]))
	answer.question_id = int(post_object["ParentId"])
	s.add(answer)

def parse_lines(gen):
	s = Session()
	for index, line in enumerate(gen):
		line = line.strip()
		if line.startswith("<row"):
			node = etree.fromstring(line)
			post_object = node.attrib

			if post_object.get('PostTypeId') == "1":
				process_questions(s, post_object)
			if post_object.get('PostTypeId') == "2":
				process_answers(s, post_object)
		if index % 2000 == 0:
			print index, "processed."
			sys.stdout.flush()

		if index % 50000 == 0:
			s.commit()
	s.commit()

def attach_foreignkeys(xml_file):
	s = Session()
	with open(xml_file,'r') as f:
		for index, line in enumerate(f):
			line = line.strip()
			if line.startswith("<row"):
				node = etree.fromstring(line)
				post_object = node.attrib

				if post_object.get('PostTypeId') == "1":
					attach_question(s, post_object)
				if post_object.get('PostTypeId') == "2":
					attach_answer(s, post_object)
			if index % 10000 == 0:
				print index, "attached."
				sys.stdout.flush()

			if index % 100000 == 0:
				s.commit()
		s.commit()


if __name__=="__main__":
	with open(sys.argv[1]) as f:
		gen = islice(f, int(sys.argv[2]), int(sys.argv[3]))
		parse_lines(gen)
		#attach_foreignkeys(sys.argv[1])

