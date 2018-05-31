#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import subprocess # to execute bash commands
  
# create a subclass and override the handler methods
res = subprocess.check_output(["pip", "install", "html2text"])

import html2text



r = requests.get("http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=RT404715658HK&Submit=Submit")
print(r.status_code)
h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
#h.ignore_tables = True
h.bypass_tables = False 
#h.body_width = 1000
h.ignore_emphasis = True 
h.ignore_emphasis = True
h.wrap_links = True 

h.pad_tables = True

raw_html=r.text
print(h.handle(raw_html))



