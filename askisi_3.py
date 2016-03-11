import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import state_union, wordnet

#Read the phrases
phrase1 = raw_input("Give one sentence: ")
phrase2 = raw_input("Give an other sentence: ")

#seperate the words of the sentences
tokenized1= word_tokenize(phrase1)
tokenized2= word_tokenize(phrase2)

#2 lists of chunked words
only1 = []
only2 = []

#___SEPERATION___
#Keep the verbs, the nouns and the adjjectives of the first sentence
try:
	for i in tokenized1:
		words = nltk.word_tokenize(i)
		tagged = nltk.pos_tag (words)
		chunkGram =  r"""Chunk: {<JJ.?>*<VB.?>*<NN.*>?}"""
		chunkParser = nltk.RegexpParser(chunkGram)
		chunked = chunkParser.parse(tagged)
		only1.append(chunked)
except Exception as e :
	print (str(e))


#Keep the verbs, the nouns and the adjjectives of the second sentence
try:
	for i in tokenized2:
		words = nltk.word_tokenize(i)
		tagged = nltk.pos_tag (words)
		chunkGram =  r"""Chunk: {<JJ.?>*<VB.?>*<NN.*>?}"""
		chunkParser = nltk.RegexpParser(chunkGram)
		chunked = chunkParser.parse(tagged)
		only2.append(chunked)
except Exception as e :
	print (str(e))


#___CREATING NEW LIST WITH THE NOUNS, VERBS, ADJ__
#Creating a new list with the words clean (1st sent)
lenFirst = len(only1)
finalList1 = []
for i in range(lenFirst):
	if Chunked in only1[i]:
		#keep cleen word without Chunked, trees, NN etc.
		temp = only1[i].lemmas()[i].name()
		finalList1.append(temp)
	

#Creating a new list with the words clean (2st sent)
lenSecond = len(only2)
finalList2 = []
for i in range(lenSecond):
	if Chunked in only2[i]:
		#keep cleen word without Chunked, trees, NN etc.
		temp = only2[i].lemmas()[i].name()
		finalList2.append(temp)

	


#___SYNONYMS___
lenFinalList1 = len(finalList1)
sum1 = 0
for i in range(lenfinalList1):
	syns = wordnet.synsets(finalList[i])
	x = len(syns)
	for j in range(x):
		if syns[j] in finalList2:
			print "one word have the same meaning with an other word of the other sent."
			sum1 += 1 


if (lenFinalList1 == sum1):
	print "The sentences have the same meaning" 

	



