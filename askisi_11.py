#Import Libraries
import requests 
from bs4 import BeautifulSoup

#___FIRST ACCOUNT___

#Read the twitter acc
url1= raw_input("Give twitter acc ")
r1 = requests.get("https://twitter.com/"  + url1 )

#Read Unable a 
soup1 = BeautifulSoup(r1.content)print int and strings in python
links = soup1.find_all("a")
for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text )

#Start the process to take all the data form twitter 
g_data_url1_1 = soup1.find_all("ul",  {"class": "ProfileNav-list"})
for item1 in g_data_url1_1:
	a_1= item1.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav"})
	b_1= item1.find_all("li", {"class": "ProfileNav-item ProfileNav-item--following"})
	c_1= item1.find_all("li", {"class": "ProfileNav-item ProfileNav-item--followers"})
	d_1= item1.find_all("li", {"class": "ProfileNav-item ProfileNav-item--favorites"})
	for tw1_1 in a_1: 
	 	tweets1= tw1_1.contents[3].text
	for fg1_1 in b_1:
		b2_1= fg1_1.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for fg2_1 in b2_1:
			following1= fg2_1.contents[3].text
	for fl1_1 in c_1:
		c2_1= fl1_1.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for fl2_1 in c2_1:
			followers1= fl2_1.contents[3].text
	for l1_1 in d_1:
		d2_1= l1_1.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for l2_1 in d2_1:
			favourites1= l2_1.contents[3].text


#___SECOND ACOUNT___

url2= raw_input("Give the other twitter acc ")
r2 = requests.get("https://twitter.com/"  + url2 )

#Read Unable a 
soup2 = BeautifulSoup(r2.content)
links = soup2.find_all("a")
for link in links:
		print "<a href='%s'>%s</a>" %(link.get("href"), link.text )

#Start the process to take all the data form twitter
g_data_url2_2 = soup2.find_all("ul",  {"class": "ProfileNav-list"})
for item2 in g_data_url2_2:
	a_2= item2.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav"})
	b_2= item2.find_all("li", {"class": "ProfileNav-item ProfileNav-item--following"})
	c_2= item2.find_all("li", {"class": "ProfileNav-item ProfileNav-item--followers"})
	d_2= item2.find_all("li", {"class": "ProfileNav-item ProfileNav-item--favorites"})		
	for tw1_2 in a_2: 
	 	tweets2= tw1_2.contents[3].text	
	for fg1_2 in b_2:
		b2_2= fg1_2.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for fg2_2 in b2_2:
			following2= fg2_2.contents[3].text				
	for fl1_2 in c_2:
		c2_2= fl1_2.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for fl2_2 in c2_2:
			followers2= fl2_2.contents[3].text
	for l1_2 in d_2:
		d2_2= l1_2.find_all("a", {"class": "ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor"})
		for l2_2 in d2_2:
			 favourites2= l2_2.contents[3].text

#___METATROPES___
#tweets
if "M" in tweets1:
	ntweets1=tweets1.replace("M", "")
	ntweets1=str(ntweets1)
	ntweets1=float(ntweets1)
	ntweets1=ntweets1*1000000
elif "K" in tweets1:
	ntweets1=tweets1.replace ("K", "")
	ntweets1=str(ntweets1)
	ntweets1=float(ntweets1)
	ntweets1=ntweets1*1000
else:
	if "," in tweets1:
		ntweets1=tweets1.replace(",", "")
		ntweets1=str(ntweets1)
		ntweets1=float(ntweets1)
	else:
		ntweets1=tweets1
		ntweets1=str(ntweets1)
		ntweets1=float(ntweets1)

if "M" in tweets2:
	ntweets2=tweets2.replace("M", "")
	ntweets2=str(ntweets2)
	ntweets2=float(ntweets2)
	ntweets2=ntweets2*1000000
elif "K" in tweets2:
	ntweets2=tweets2.replace ("K", "")
	ntweets2=str(ntweets2)
	ntweets2=float(ntweets2)
	ntweets2=ntweets2*1000
else:
	if "," in tweets2:
		ntweets2=tweets2.replace(",", "")
		ntweets2=str(ntweets2)
		ntweets2=float(ntweets2)
	else:
		ntweets2=tweets2
		ntweets2=str(ntweets2)
		ntweets2=float(ntweets2)

#following
if "M" in following1:
	nfollowing1=following1.replace("M", "")
	nfollowing1=str(nfollowing1)
	nfollowing1=float(nfollowing1)
	nfollowing1=nfollowing1*1000000
elif "K" in following1:
	nfollowing1=following1.replace ("K", "")
	nfollowing1=str(nfollowing1)
	nfollowing1=float(nfollowing1)
	nfollowing1=nfollowing1*1000
else:
	if "," in following1:
		nfollowing1=following1.replace(",", "")
		nfollowing1=str(nfollowing1)
		nfollowing1=float(nfollowing1)
	else:
		nfollowing1=following1
		nfollowing1=str(nfollowing1)
		nfollowing1=float(nfollowing1)

if "M" in following2:
	nfollowing2=following2.replace("M", "")
	nfollowing2=str(nfollowing2)
	nfollowing2=float(nfollowing2)
	nfollowing2=nfollowing2*1000000
elif "K" in following2:
	nfollowing2=following2.replace ("K", "")
	nfollowing2=str(nfollowing2)
	nfollowing2=float(nfollowing2)
	nfollowing2=nfollowing2*1000
else:
	if "," in following2:
		nfollowing2=following2.replace(",", "")
		nfollowing2=str(nfollowing2)
		nfollowing2=float(nfollowing2)
	else:
		nfollowing2=following2
		nfollowing2=str(nfollowing2)
		nfollowing2=float(nfollowing2)


#followers
if "M" in followers1:
	nfollowers1=followers1.replace("M", "")
	nfollowers1=str(nfollowers1)
	nfollowers1=float(nfollowers1)
	nfollowers1=nfollowers1*1000000
elif "K" in followers1:
	nfollowers1=followers1.replace ("K", "")
	nfollowers1=str(nfollowers1)
	nfollowers1=float(nfollowers1)
	nfollowers1=nfollowers1*1000
else:
	if "," in followers1:
		nfollowers1=followers1.replace(",", "")
		nfollowers1=str(nfollowers1)
		nfollowers1=float(nfollowers1)
	else:
		nfollowers1=followers1
		nfollowers1=str(nfollowers1)
		nfollowers1=float(nfollowers1)

if "M" in followers2:
	nfollowers2=followers2.replace("M", "")
	nfollowers2=str(nfollowers2)
	nfollowers2=float(nfollowers2)
	nfollowers2=nfollowers2*1000000
elif "K" in followers2:
	nfollowers2=followers2.replace ("K", "")
	nfollowers2=str(nfollowers2)
	nfollowers2=float(nfollowers2)
	nfollowers2=nfollowers2*1000
else:
	if "," in followers2:
		nfollowers2=followers2.replace(",", "")
		nfollowers2=str(nfollowers2)
		nfollowers2=float(nfollowers2)
	else:
		nfollowers2=followers2
		nfollowers2=str(nfollowers2)
		nfollowers2=float(nfollowers2)

#likes
if "M" in favourites1:
	nfavourites1=favourites1.replace("M", "")
	nfavourites1=str(nfavourites1)
	nfavourites1=float(nfavourites1)
	nfavourites1=nfavourites1*1000000
elif "K" in favourites1:
	nfavourites1=favourites1.replace ("K", "")
	nfavourites1=str(nfavourites1)
	nfavourites1=float(nfavourites1)
	nfavourites1=nfavourites1*1000
else:
	if "," in favourites1:
		nfavourites1=favourites1.replace(",", "")
		nfavourites1=str(nfavourites1)
		nfavourites1=float(nfavourites1)
	else:
		nfavourites1=favourites1
		nfavourites1=str(nfavourites1)
		nfavourites1=float(nfavourites1)

if "M" in favourites2:
	nfavourites2=favourites2.replace("M", "")
	nfavourites2=str(nfavourites2)
	nfavourites2=float(nfavourites2)
	nfavourites2=nfavourites2*1000000
elif "K" in favourites2:
	nfavourites2=favourites2.replace ("K", "")
	nfavourites2=str(nfavourites2)
	nfavourites2=float(nfavourites2)
	nfavourites2=nfavourites2*1000
else:
	if "," in favourites2:
		nfavourites2=favourites2.replace(",", "")
		nfavourites2=str(nfavourites2)
		nfavourites2=float(nfavourites2)
	else:
		nfavourites2=favourites2
		nfavourites2=str(nfavourites2)
		nfavourites2=float(nfavourites2)


#___CHECK___
acc1=0
acc2=0

if (ntweets1<ntweets2):
	acc2=acc2+1
else:
	acc1=acc1+1

if (nfollowing1<nfollowing2):
	acc2=acc2+1
else:
	acc1=acc1+1

if (nfollowers1<nfollowers2):
	acc2=acc2+1
else:
	acc1=acc1+1

if (nfavourites1<nfavourites2):
	acc2=acc2+1
else:
	acc1=acc1+1


print "the score is: ", acc1, "-", acc2