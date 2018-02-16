#!/usr/bin/python3
import requests
import subprocess # to execute bash commands
import sys
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

try:
    tracking_number = str(sys.argv[1])

except(IndexError, ValueError):
    print("please enter a tracking number of a valid format")
    sys.exit(2)    

request_url = "http://ipsweb.ptcmysore.gov.in/ipswebtracking/IPSWeb_item_events.asp?itemid=" + tracking_number
#print(request_url)
r = requests.get(request_url)
print(r.status_code)

f = open("raw_html", "w+")
f.write(r.text)
f.close()

view_html = subprocess.Popen(["html2text", "raw_html"])
output = view_html.communicate()
view_html.wait()
print(output)
