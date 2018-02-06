#!/usr/bin/python3

#trial using bash calls no html2text library

import requests
import subprocess # to execute bash commands


try:
    check_for_package = subprocess.Popen(("dpkg","-s","html2text"), stdout=subprocess.PIPE) 
    output = subprocess.check_output(("grep", "Status"), stdin=check_for_package.stdout)
    check_for_package.wait()
    opstr=str(output, 'utf-8')
    print(opstr)
    if opstr == "Status: install ok installed\n" :
        print("Package installed")

except:
    print("installing html2text..............................")
    install_pkg = subprocess.check_call("sudo apt install html2text", shell=True)




r = requests.get("http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=RT404715658HK&Submit=Submit")
print(r.status_code)

raw_html=r.text
#print(raw_html)
#raw_html = str(raw_html , 'utf-8')

view_html = subprocess.Popen(["html2text", raw_html])
output = view_html.communicate()
view_html.wait()
#view_html = subprocess.Popen("html2text template", shell=True)
print(output)


