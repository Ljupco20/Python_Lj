import requests
from bs4 import BeautifulSoup
import re

link = "http://python-data.dr-chuck.net/comments_144908.html"

reuest = requests.get(link)
soup = BeautifulSoup(reuest.text,"lxml")

soupl=soup.findAll("span", { "class" : "comments" })
sum=0

for item in soupl:
    sum = sum + int(item.text)

print(sum)