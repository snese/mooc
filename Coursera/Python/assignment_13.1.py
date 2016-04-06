# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_245524.xml (Sum ends with 32)
#
# Data Format and Approach
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>

import urllib
import xml.etree.ElementTree as ET

while True:
	url = raw_input('Enter URL: ')
	if len(url) > 1 : break

print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

results = tree.findall('.//count')

counts = 1
sum = 0

for idx in range(len(results)):
	sum += int(results[idx].text)
	counts += 1

print "Count:",counts
print "Sum:",sum
