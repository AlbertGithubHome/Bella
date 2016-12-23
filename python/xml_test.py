#xml test

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_elemnet: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s', name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

#parser
handler = DefaultSaxHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'python')
#L.append(encode('some & data'))
L.append(r'</root>')

myXML = ''.join(L)
print('MyXML =', myXML)