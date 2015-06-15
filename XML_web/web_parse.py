#!/usr/bin/python
from xml.sax.handler import ContentHandler
from xml.sax import parse

class Web_Maker(ContentHandler):
    pass_through = False
    def __init__(self):
        ContentHandler.__init__(self)
        self.data = []

    def startElement(self,name,attrs):
        if name== 'page':
	   self.pass_through = True
	   self.out = open(attrs['name']+'.html','w')
	   self.out.write('<html><head>\n')
	   self.out.write('<title>%s</title\n>'% attrs['title'])
	   self.out.write('</head><body>')
	elif self.pass_through:
	   self.out.write('<'+name)
	   for key,val in attrs.items():
               self.out.write(' %s="%s"' % (key,val))
	   self.out.write('>')

    def endElement(self,name):
	if name == 'page':
	    self.pass_through = False
	    self.out.write('\n</body></html>\n')
	    self.out.close()
	elif self.pass_through:
	    self.out.write('</%s>' % name)

    def characters(self,string):
	if self.pass_through:
	    self.out.write(string)
    

parse('website.xml',Web_Maker())


