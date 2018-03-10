# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:28:54 2018

@author: huika
"""

import urllib
from bs4 import BeautifulSoup

url = "https://www.upcdatabase.com/item/"
code = "0070792011706"

content = urllib.request.urlopen(url + code).read()

soup = BeautifulSoup(content, 'html.parser')
psoup = soup.prettify()
item = soup.find_all('td')
it = str(item[8]).split(">")
it2 = it[1].split("<")

final_it = it2[0]

print(final_it)