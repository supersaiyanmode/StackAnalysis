from lxml  import etree

def parse_xml_file(xml_file):
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
                    print "key = "+key+" " +node.attrib[key],

if __name__=="__main__":
    parse_xml_file('post_out.xml')
