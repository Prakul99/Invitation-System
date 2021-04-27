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

print "content-type: text/html"
print
print "<html><body>"
print '<form action= "deleteCookies.cgi" method="POST">'
print '<label for="clearMessage">Hi</label>'
print ''
print cookie.get('firstname')
print ''
print '<label for="clearMessage">.You have chose to ATTEND the event.You can close this tab now.</label><br>'
print '<input type="submit" value="Anonymize">'
print '</form>'
print '<br>'
print '<p>Congratulations you are coming. :)</p>'
print '<br>'
print '<form action= "updateStatus.cgi" method="POST">'
print    '<br><label for="firstname">If you are not able to come please mark "No" below. </label><br>'
print      '<input type="checkbox" id="no" name="status" value="no">'
print      '<label for="no">No</label><br><br>'
print      '<input type="submit" value="Submit">'
print '</form>'
print "</body></html>"
