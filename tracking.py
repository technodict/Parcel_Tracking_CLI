#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re

r = requests.get("http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=RT404715658HK&Submit=Submit")
print(r.status_code)
#print(r.text)
html = r.text

soup_html = BeautifulSoup(html, 'html.parser')
#print(soup_html)
#print(soup_html.prettify())
#print (parsed_html.body.__find('div', attrs={'class':'container'}).text)
html_to_parse = soup_html.prettify()


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
        #print ("Encountered a start tag:", tag)
    #def handle_endtag(self, tag):
        #print ("Encountered an end tag :", tag)
    def handle_data(self, data):
        #print ("Encountered some data  :", data)
        print(data)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
#print(parser.feed(html_to_parse))
html_raw = parser.feed(html_to_parse)
regex = re.compile(r"\s*(<[^<>]+>)\s*")
html_final = regex.sub("\g<1>", html_raw)
print(html_final)

