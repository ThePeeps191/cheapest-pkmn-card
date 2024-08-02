import requests
from bs4 import BeautifulSoup

def scrape(s):
	s = s.lower().replace(" ", "+")
	base1 = "https://www.ebay.ca/sch/i.html?_from=R40&_nkw="
	base2 = "+-code+-online+-finish+-pick+-codes+-email+-ptcgo+-email+-universe+-v+-digital&_sacat=0&_sop=15&_blrs=recall_filtering&rt=nc&LH_BIN=1"
	base3 = "+-code+-online+-finish+-pick+-codes+-email+-ptcgo+-email+-digital&_sacat=0&_sop=15&_blrs=recall_filtering&rt=nc&LH_BIN=1"
	if "vstar" in s:
		r = requests.get(base1 + s + base2)
	else:
		r = requests.get(base1 + s + base3)
	w = BeautifulSoup(r.text, "html.parser")
	links = w.find_all('ul', attrs={'class': 'srp-results'})
	l = links[0]
	l2 = str(l).split('href="')[1].split('"')[0]
	if l2 != "#icon-save-small":
		return l2
	else:
		return -1