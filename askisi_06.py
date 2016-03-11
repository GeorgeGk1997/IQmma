#Import Libraries
import requests 
from bs4 import BeautifulSoup

#Obtain the date
date = raw_input("Give the date in this form dd-mm-yyyy: ")
req = requests.get("http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + date + ".json")

#Read the code of the page and save it 
soup = BeautifulSoup(req.content)
sample_text = soup.text 
sample_text = str(sample_text)
length = len(sample_text)

#Creating a list in which i will store all the numbers that appeared this day
finalList = []
for i in range(length):
	k=i+1
	if (sample_text[i]  == "r" and sample_text[k] == "e" ):
		iTemp = i
		iTemp = iTemp + 9 
		var = ""
		num = 0
		while (sample_text[iTemp] != "]"):
			if (num != 0):
				finalList.append(num)
			iTemp = iTemp + 1 
			var = ""
			num = 0
			while (sample_text[iTemp] != ","):
				var = str(num)
				tempVar = sample_text[iTemp]
				var = var + tempVar
				num = int(var)
				if (sample_text[iTemp+1] == "]"):
					iTemp = iTemp +1
					break
				iTemp = iTemp + 1	
		if (num != 0):
			finalList.append(num)

#Run all the list and find out how many times a number appears
pointer = 1
listLen = len(finalList)
while (pointer<=80):
	sameNum = 0
	for i in range(listLen):
		if (finalList[i] == pointer):
			sameNum = sameNum +1
	print "the number -", pointer, "- it appears ", sameNum, "times"
	pointer = pointer + 1
	
