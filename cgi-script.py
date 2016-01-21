#!/usr/bin/env python

import os, json, cgi

print "Content-type: text/html"
print 
print "<html><body><h1>Hello, world!</h1>"
print "<form method='POST'><input name='x'></form>"

form = cgi.FieldStorage()
print "<p>X was: " + cgi.escape(str(form.getvalue('x'))) + "</p>"

print json.dumps(dict(os.environ), indent = 4)

print "</body></html>"
