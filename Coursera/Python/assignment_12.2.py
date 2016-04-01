# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Kieryn.html

import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

position = int(raw_input('Enter position: '))
count = int(raw_input('Enter count: '))

print "Retrieving:",url

while count > 0:
	tags = soup('a')
	print "Retrieving:",tags[position - 1].get('href', None)
	url = tags[position - 1].get('href', None)
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	count -= 1

print "Last Name:",re.findall(r"[A-Z][a-z]+",url)[0]
