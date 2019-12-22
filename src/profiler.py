'''
Parses the given text file. 

'''

import re
import math

class Profiler:
	'''
	Gets the profile the text. 
	Eg. Average length of sentences, conjIndex, ppIndex etc. 
	'''
	def __init__(self):
		print("A Profiler object created")

	def getProfile(self, textFilePath, author): #Reads text file
		profile=dict()
		with open(textFilePath, 'r') as textFile:
			data=textFile.read().replace('\n', '')
			data=data.strip()
			data=data.split('.')

		textFile.close
		profile['avgLength']=self.getAvgLength(data)
		profile['avgWordLength'] = self.getAvgWordLength(data)
		profile['variance']=self.getArticleIndex(data)
		profile['author']=author
		profile['ppIndex']=self.getppIndex(data)
		profile['conjIndex']=self.getConjIndex(data)
		profile['prepIndex']=self.getPrepIndex(data)
		profile['articleIndex']=self.getVariance(data)
		profile['commaIndex']=self.getCommaIndex(data)
		return profile

	def getAvgLength(self, data): # Filters proper sentences, removes empty strings, and gets the length. 
		pattern=re.compile('')
		lengthList=[]
		for sentences in data:
			sentences=sentences.split(' ')
			if len(sentences)>3:
				lengthList.append(len(sentences))
		#print(lengthList)
		return self.calculateAvg(lengthList)

	def getAvgWordLength(self, data):
		'''
		Returns the average length of the words.
		'''
		total=0
		words=[]
		for sentence in data:
			words.extend(sentence.split())
		for word in words:
			total=total+len(word)
		return (total/len(words))	

	def calculateAvg(self, lengthList):
		total=0
		for length in lengthList:
			total=total+length
		return (total/len(lengthList))

	def getppIndex(self, data):
		'''
		Returns the number of personal pronouns used per 100 words.
		'''
		personalPronouns=[]
		with open('pivotFiles/personalPronouns.txt', 'r') as textFile: # Read the list of pronouns
			for pronouns in textFile:
				personalPronouns.append(pronouns.strip())

		totalWords=0
		totalPersonalPronouns=0
		for sentences in data:
			words=sentences.split(' ')
			for word in words:
				totalWords=totalWords+1
				if word.lower() in personalPronouns:
					totalPersonalPronouns=totalPersonalPronouns+1
		return totalPersonalPronouns*100/totalWords

	def getConjIndex(self, data):
		'''
		Returns the number of conjunctions used per 100 words.
		'''
		conjList=[]
		with open('pivotFiles/conjunctions.txt', 'r') as textFile: # Read the list of pronouns
			for conj in textFile:
				conjList.append(conj.strip().lower())

		totalWords=0
		totalConj=0
		for sentences in data:
			words=sentences.split(' ')
			for word in words:
				totalWords=totalWords+1
				if word.lower() in conjList:
					totalConj=totalConj+1
		return totalConj*100/totalWords

	def getPrepIndex(self, data):
		prepList=[]
		with open('pivotFiles/prepositions.txt', 'r') as textFile: # Read the list of pronouns
			for prep in textFile:
				prepList.append(prep.strip().lower())

		totalWords=0
		totalPrep=0
		for sentences in data:
			words=sentences.split(' ')
			for word in words:
				totalWords=totalWords+1
				if word.lower() in prepList:
					totalPrep=totalPrep+1
		return totalPrep*100/totalWords

	def getArticleIndex(self, data):
		articleList=['a','an','the']
		totalWords=0
		totalArticles=0
		for sentences in data:
			words=sentences.split(' ')
			for word in words:
				totalWords=totalWords+1
				if word.lower() in articleList:
					totalArticles=totalArticles+1
		return totalArticles*100/totalWords

	def getVariance(self, data):
		pattern=re.compile('')
		lengthList=[]
		for sentences in data:
			sentences=sentences.split(' ')
			if len(sentences)>3:
				lengthList.append(len(sentences))
		total=0
		for length in lengthList:
			total=total+length
		avg=total/len(lengthList)

		varianceSum=0
		for length  in lengthList:
			varianceSum=varianceSum+pow((avg-length),2)
		variance=math.sqrt(varianceSum/len(lengthList))
		return variance

	def getCommaIndex(self, data):
		comma=','
		totalWords=0
		totalCommas=0
		for sentences in data:
			words=sentences.split(' ')
			for word in words:
				totalWords=totalWords+1
				if comma in word:
					totalCommas=totalCommas+1
		return totalCommas*100/totalWords
		



