from lxml  import etree
import sqlite3
from schema import Posts, Users, Questions, Answers, Tags, Session
import  re


def parse_xml_file(xml_file):

    post_object = {}

    with open(xml_file,'r') as f:
        for x in f:
            x = x.strip()
            if x.startswith("<row"):
                node = etree.fromstring(x)
                
                for key in node.keys():
                  
                    post_object[key] = node.attrib[key]    
                  
                print " PRINTING THE RECORDS NOW "
                posts = Posts(post_object.get('Id'),post_object.get('PostTypeId'),post_object.get('AcceptedAnswerId'),post_object.get('ParentId'),post_object.get('CreationDate'),post_object.get('Score'),post_object.get('OwnerUserId'),post_object.get('LastActivityDate'),post_object.get('Tags'),post_object.get('AnswerCount'))
 
                
                s = Session()
                if post_object.get('PostTypeId') == str(1):
                    questions = Questions(post_object.get('Id'),post_object.get('PostTypeId'),post_object.get('AcceptedAnswerId'),post_object.get('CreationDate'),post_object.get('Score'),post_object.get('OwnerUserId'),post_object.get('LastActivityDate'),post_object.get('Tags'),post_object.get('AnswerCount'))
                    print "tags = ", post_object.get('Tags')
                    if post_object.get('Tags') is not None:
                        print "inside"
                        str_ =  re.findall("\<(.*?)\>", post_object.get('Tags'))
                        for x in str_:
                            print "x = ",x
                            tag = s.query(Tags).filter_by(TagName = x).first()
                            if not tag:
                                tag = Tags(x)
                            tag.questions.append(questions)
                            s.add(tag)

                        s.commit()    
                    else: 
                        s.add(questions)
                        s.commit()
                 
                if post_object.get('PostTypeId') == str(2):
                    answers = Answers(post_object.get('Id'),post_object.get('PostTypeId'),post_object.get('ParentId'),post_object.get('CreationDate'),post_object.get('Score'),post_object.get('OwnerUserId'),post_object.get('LastActivityDate'))
                    s.add(answers)
                    s.commit()
   

                post_object = {}

'''    create_posts_schema(list_of_fields)'''


'''
The fields in the Posts.xml are :
['Id', 'PostTypeId', 'AcceptedAnswerId', 'CreationDate', 'Score', 'ViewCount', 'Body', 'OwnerUserId', 'LastEditorUserId', 'LastEditorDisplayName', 'LastEditDate', 'LastActivityDate', 'Title', 'Tags', 'AnswerCount', 'CommentCount', 'FavoriteCount', 'CommunityOwnedDate']

'''








if __name__=="__main__":

   parse_xml_file('post_out.xml')
  
   
   
