import re

from lxml import etree
from dateutil import parser

from data import Posts, Users, Questions, Answers, Tags, Session

def process_questions(s, post_object):
    arr = ['Id', 'PostTypeId', 'AcceptedAnswerId', 'CreationDate', 'Score',
            'OwnerUserId', 'LastActivityDate', 'AnswerCount']
    params = {x: post_object.get(x) for x in arr}
    params['CreationDate'] = parser.parse(params['CreationDate'])
    params['LastActivityDate'] = parser.parse(params['LastActivityDate'])
    questions = Questions(**params)
    if post_object.get('Tags') is not None:
        tags = re.findall("\<(.*?)\>", post_object.get('Tags'))
        for tag in tags:
            tag_obj = s.query(Tags).filter_by(TagName=x).first()
            if not tag_obj:
                tag_obj = Tags(TagName=x)
            tag_obj.questions.append(questions)
            s.add(tag_obj)
        s.commit()    
    else:
        s.add(questions)
        s.commit()

def process_answers(s, post_object):
    arr = ['Id', 'PostTypeId', 'ParentId', 'CreationDate', 'Score',
            'OwnerUserId', 'LastActivityDate']
    params = {x: post_object.get(x) for x in arr}
    params['CreationDate'] = parser.parse(params['CreationDate'])
    params['LastActivityDate'] = parser.parse(params['LastActivityDate'])
    answers = Answers(**params)
    s.add(answers)
    s.commit()

def parse_xml_file(xml_file):
    s = Session()
    with open(xml_file,'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("<row"):
                node = etree.fromstring(line)
                post_object = node.attrib

                if post_object.get('PostTypeId') == str(1):
                   process_questions(s, post_object)
                if post_object.get('PostTypeId') == str(2):
                   process_answers(s, post_object)


if __name__=="__main__":
   parse_xml_file('post_out.xml')

