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

import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
r = requests.get(url)
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

#print(soup.prettify())

for word in soup.find_all(class_="page"):
	for words in word.find_all("field-item"):
		if word.field-item:
			print(word.field-item.text.replace("sudent", "AMAZING student"))


#cant get it to print anything
	# beautifulsoup 
	# beautify
	# replace it 
	# then apparently turning it into a html sfvidf