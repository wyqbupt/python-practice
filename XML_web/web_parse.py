#!/usr/bin/python
from xml.sax.handler import ContentHandler
from xml.sax import parse
import os
class Dispatch:
    
    def startElement(self,name,attrs):
        self.dispatch('start',name,attrs)
    
    def endElement(self,name):
        self.dispatch('end',name)
    
    def dispatch(self,prefix,name,attrs=None):
        method_name = prefix+name.capitalize()
        default_method_name = 'default'+prefix.capitalize()
        method = getattr(self,method_name,None)
        if callable(method):
            args = ()
        else:
            method = getattr(self,default_method_name,None)
            args = name,
        if prefix == 'start':
            args+=attrs,
        if callable(method):
            method(*args)

class Web_Maker(Dispatch,ContentHandler):
    
    pass_through = False
    
    def __init__(self,directory):
        ContentHandler.__init__(self)
        self.directory= [directory]
        self.ensureDirectory()

    def writeHeader(self,title):
        self.out.write("<html\n><head>\n<title>")
        self.out.write(title)
        self.out.write("</title>\n </head>\n <body>\n")
    
    def writeFooter(self):
        self.out.write("\n </body>\n</html>\n")
    
    def defaultStart(self,name,attrs):
        if self.pass_through:
            self.out.write('<'+name)
            for key,val in attrs.items():
                self.out.write(' %s="%s"' % (key,val))
            self.out.write('>')
    
    def defaultEnd(self,name):
        if self.pass_through:
            self.out.write("</%s>" % name)

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def characters(self,chars):
	if self.pass_through:
	    self.out.write(chars)
    
    def startDirectory(self,attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()
    
    def endDirectory(self):
        self.directory.pop()
    
    def startPage(self,attrs):
        filename = os.path.join(*self.directory+[attrs['name']+'.html'])
        self.out= open(filename,'w')
        self.writeHeader(attrs['title'])
        self.pass_through = True
    
    def endPage(self):
        self.pass_through = False
        self.writeFooter()
        self.out.close()

parse('website.xml',Web_Maker('public_html'))

