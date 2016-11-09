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

fout = open('output.html','w')
url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
#r = requests.get(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

k = soup.prettify()

namechange = re.sub("student", "AMAZING student", k)

fout.write(namechange)


#cant get it to print anything
	# beautifulsoup 
	# beautify
	# replace it 
	# then apparently turning it into a html sfvidf