# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.
# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import re
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)



url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(r.text, "html.parser")

for mypic in soup.findall("img"):
	mypic_tags = mypic['src']
	if "logo2.png" not in mypic_tags:
		img['src'] = 'C:\Users\Dr\Desktop\206proj3\SI206\HW3-StudentCopy\media\pic_of_me.JPG'
	else:
		img['src']= 'C:\Users\Dr\Desktop\206proj3\SI206\HW3-StudentCopy\media\logo.png'

k = soup.prettify()

namechange = re.sub("student", "AMAZING student", k)

fout = open('output.html','w')
fout.write(namechange)
fout.close()

