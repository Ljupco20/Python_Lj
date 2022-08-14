# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
coun=input('Enter your count:')
pos=input('Enter your position:')
#print(url)

for i in range(int(coun)):
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html,"html.parser")
  tags = soup('a')
  url = tags[int(pos)-1].get('href',None)
print (url)