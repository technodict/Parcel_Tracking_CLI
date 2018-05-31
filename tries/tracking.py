#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

r = requests.get("http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=RT404715658HK&Submit=Submit")
print(r.status_code)
#print(r.text)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
title_box = soup.find('title')
title = title_box.text.strip()
print(title)

track_no = soup.find('strong')
track_no = track_no.text.strip()
print('TRACKING NUMBER IS :', track_no)

for tr in soup.find_all('tr')[2:]:
    tds=tr.find_all('td')
    print (tds[0].text, tds[1].text, tds[2].text)
