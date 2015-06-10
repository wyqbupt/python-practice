#!/usr/bin/python
from xml.sax.handler import ContentHandler
from xml.sax import parse

class Web_Handler(ContentHandler):
    def startElement(self,name,attrs):
        print name,attrs.keys()

parse('website.xml',Web_Handler())

