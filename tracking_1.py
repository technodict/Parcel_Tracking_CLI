#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re

# create a subclass and override the handler methods

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
    def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)



r = requests.get("http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=RT404715658HK&Submit=Submit")
print(r.status_code)
raw_html = r.text
#print(raw_html)
#data_element = MyHTMLParser.handle_startendtag(</script>)
#print(data_element)
#result = MLStripper.strip_tags(html)
#print(result)

soup = BeautifulSoup(raw_html, "lxml")
title = soup.title.text
print(title)
data = soup.tbody.text
print(data)
#print(soup.get_text())






