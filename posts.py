from lxml  import etree
import sqlite3
import data, re


def parse_xml_file(xml_file):
    list_of_fields = []
    post_object = {}
    field_counter = 0
    with open(xml_file,'r') as f:
        for x in f:
            x = x.strip()
            if x.startswith("<row"):
                node = etree.fromstring(x)
                
                for key in node.keys():
                  
                    post_object[key] = node.attrib[key]    
                  
                print " PRINTING THE RECORDS NOW "
                # print post_object    
                posts = data.Posts(post_object.get('Id'),post_object.get('PostTypeId'),post_object.get('AcceptedAnswerId'),post_object.get('ParentId'),post_object.get('CreationDate'),post_object.get('Score'),post_object.get('OwnerUserId'),post_object.get('LastActivityDate'),post_object.get('Tags'),post_object.get('AnswerCount'))
 
                
                s = data.Session()
                print "tags = ", post_object.get('Tags')
                if post_object.get('Tags') is not None:
                    print "inside"
                    str =  re.findall("\<(.*?)\>", post_object.get('Tags'))
                    for x in str:
                        print "x = ",x
                        tag = s.query(data.Tags).filter_by(TagName = x).first()
                        if not tag:
                            tag = data.Tags(x)
                        tag.posts.append(posts)
                        s.add(tag)

                    s.commit()    
                else: 


                    s.add(posts)

                    s.commit()
   

                post_object = {}

'''    create_posts_schema(list_of_fields)'''


'''
The fields in the Posts.xml are :
['Id', 'PostTypeId', 'AcceptedAnswerId', 'CreationDate', 'Score', 'ViewCount', 'Body', 'OwnerUserId', 'LastEditorUserId', 'LastEditorDisplayName', 'LastEditDate', 'LastActivityDate', 'Title', 'Tags', 'AnswerCount', 'CommentCount', 'FavoriteCount', 'CommunityOwnedDate']

'''

def select_from_post():
    with data.engine.connect() as con:
        rs = con.execute('Select * from posts')
        print " SELECT DATA FROM POSTS "
        for row in rs:
            print row


def delete_from_post():
    data.Session.query(data.Posts).delete()
    data.Session().commit()


def create_posts_schema(columns):
    conn = sqlite3.connect('post.db')
    c = conn.cursor()
    c.execute('CREATE TABLE') 

if __name__=="__main__":
   # parse_xml_file  parses the xml file and inserts records in the posts table 
   parse_xml_file('post_out.xml')
   # delete_from_post() deletes the all records from the posts table
   # delete_from_post()
   # select_from_post() selects and prints records from the table 
   #select_from_post()
