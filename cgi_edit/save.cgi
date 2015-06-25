#!/usr/bin/env python

from os.path import join,abspath
import cgi,sys,sha

print 'Content-type: text/html\n'

BASE_DIR = abspath('data')
form = cgi.FieldStorage()

filename = form.getvalue('filename')
password = form.getvalue('password')

if not filename:
    print 'Please enter a file name'
    sys.exit()
if sha.sha(password).hexdigest() != '8843d7f92416211de9ebb963ff4ce2812593287    8':
    print 'Invalid parameters.'
    sys.exit()

f = open(join(BASE_DIR.filename),'w')
f.write(text)
f.close()
print 'The file has been saved.'

