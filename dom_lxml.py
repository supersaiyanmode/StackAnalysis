from lxml  import etree
import sqlite3
import data


def parse_xml_file(xml_file):
    list_of_fields = []
    post_object = {}
    field_counter = 0
    with open(xml_file,'r') as f:
        for x in f:
            x = x.strip()
            if x.startswith("<row"):
                node = etree.fromstring(x)
                '''
                print node.get('Body')
                '''
                '''
                print node.attrib 
                '''
                '''
                print node.keys()
                '''
                for key in node.keys():
                    if (field_counter == 0):
                        list_of_fields.append(key)
                    post_object[key] = node.attrib[key]    
                    '''
                    print "key = "+key+" " +node.attrib[key],
                '''    
                post_object.setdefault('ParentId',-1)
                post_object.setdefault('PostTypeId',-1)
                post_object.setdefault('AcceptedAnswerId',-1)
                post_object.setdefault('CreationDate',"")
                post_object.setdefault('Score',-1)
                post_object.setdefault('OwnerUserId',-1)
                post_object.setdefault('LastActivityDate',"")
                post_object.setdefault('Tags',"")
                post_object.setdefault('AnswerCount',-1)
                print " PRINTING THE RECORDS NOW "
                print post_object    
                posts = data.Posts(post_object['Id'],post_object['PostTypeId'],post_object['AcceptedAnswerId'],post_object['ParentId'],post_object['CreationDate'],post_object['Score'],post_object['OwnerUserId'],post_object['LastActivityDate'],post_object['Tags'],post_object['AnswerCount'])
                s = data.Session()
                s.add(posts)
                s.commit()
                print post_object    
                field_counter += 1
                post_object = {}
    print list_of_fields
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
    data.Session.query(posts).delete()


def create_posts_schema(columns):
    conn = sqlite3.connect('post.db')
    c = conn.cursor()
    c.execute('CREATE TABLE') 

if __name__=="__main__":
   # parse_xml_file('post_out.xml')
   delete_from_post()
   select_from_post()
