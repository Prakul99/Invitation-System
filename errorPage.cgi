#!/usr/bin/python

import sys
import os
from os import environ

# if environ.has_key('HTTP_COOKIE'):
#     for c in environ['HTTP_COOKIE'].split(';'):
#         (key,value) = c.split('=',1)
#         key = key.strip(" ")
#         value = value.strip(" ")
#         cookie[key] = value

print "content-type: text/html"
print
print "<html><body>"
print '<form action= "welcome.cgi" method="POST">'
print '<label for="errorReturn">There is something wrong with your code.</label><br>'
print '<label for="errorReturn">The reasons can be the following,</label><br>'
print '<label for="errorReturn">1. Your name is not valid.</label><br>'
print '<label for="errorMessage">  Note: Your name must include an alphabet to be valid.</label><br>'
print '<label for="errorReturn">2. You did not marked any YES or NO in your form.</label><br>'
print '<input type="submit" value="Go Back">'
print '</form>'
print "</body></html>"
