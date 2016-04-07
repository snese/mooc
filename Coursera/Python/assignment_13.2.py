# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_245528.json (Sum ends with 74)
#
# Data Format
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
import urllib
import json

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(data)
    print 'User count:', len(info['comments'])
    sum = 0

    for item in info['comments']:
        sum += item['count']
    print 'Sum', sum

