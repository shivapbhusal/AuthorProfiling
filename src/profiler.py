'''
Parses the given text file. 

'''

import re

class Profiler:
	'''
	Gets the profile the text. 
	Eg. Average length of senteces, ratio of nouns, 
	ratio of verbs, use of narrations etc. 
	'''
	def __init(self):
		print("A Profiler object created")

	def getProfile(self, textFilePath, author): #Reads text file
		profile=dict()
		with open(textFilePath, 'r') as textFile:
			data=textFile.read().replace('\n', '')
			data=data.strip()
			data=data.split('.')
		textFile.close
		profile['avgLength']=self.getAvgLength(data)
		profile['author']=author
		profile['personalPronouns']=self.getPersonalPronouns(data)
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

	def calculateAvg(self, lengthList):
		total=0
		for length in lengthList:
			total=total+length
		return (total/len(lengthList))

	def getPersonalPronouns(self, data):
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
		return totalPersonalPronouns/totalWords


p=Profiler()
print(p.getProfile('testData/Dikens/greatExpectations.txt','Dikens'))
print(p.getProfile('testData/Chekhov/stories.txt','Chekhov'))
