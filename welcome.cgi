#!/usr/bin/python

import sys
import os
from os import environ

cookie = {}

if environ.has_key('HTTP_COOKIE'):
    for c in environ['HTTP_COOKIE'].split(';'):
        (key,value) = c.split('=',1)
        key = key.strip(" ")
        value = value.strip(" ")
        cookie[key] = value


cookieDeleted = True


if cookie.get('firstname') == '~':
    cookieDeleted = False


print "content-type: text/html"
print
print "<html> <body>"
if cookieDeleted and 'firstname' in cookie and cookie.get('status') == 'yes':
    print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=http://www-test.cs.umanitoba.ca/~prakul/cgi-bin/reply.cgi">'   
elif cookieDeleted and 'firstname' in cookie and cookie.get('status') == 'no':     
    print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=http://www-test.cs.umanitoba.ca/~prakul/cgi-bin/notAccept.cgi">'             
else:     
    print '<form action= "myScript.cgi" method="POST">'
    print    '<label for="firstname">Full name:</label><br> <input type="text" id="firstname" name="firstname"><br>'
    print     '<p>Would you like to come?</p>'
    print      '<input type="radio" id="yes" name="status" value="yes">'
    print      '<label for="yes">Yes</label><br>'
    print      '<input type="radio" id="no" name="status" value="no">'
    print      '<label for="no">No</label><br><br>'
    print      '<input type="submit" value="Submit">'
    print '</form>'
print "</body></html>"

