'''
Implementation of K-Nearest Neighbour classifier
'''
import ast
import os
import math
import profiler as profiler

class KNN:
	def __init__(self, kValue):
		self.K=kValue

	def classify(self, newProfile):
		existingProfiles=open('results/authorProfiles.txt')
		allDistances=dict()
		for lines in existingProfiles:
			lines=lines.strip()
			existingProfile=ast.literal_eval(str(lines))
			distance=self.getEuclidianDistance(newProfile, existingProfile)
			allDistances[distance]=existingProfile['author']
		keys=list(allDistances.keys())
		keys.sort()
		kNeighbours=[]
		for i in range(self.K):
			kNeighbours.append(allDistances[keys[i]])
		#print(kNeighbours)
		print(self.getClass(kNeighbours))
			
	def getEuclidianDistance(self,newProfile, existingProfile):
		avgConjDiff=pow((newProfile['conjIndex']-existingProfile['conjIndex']),2)
		avgLengthDiff=pow((newProfile['avgLength']-existingProfile['avgLength']),2)
		varianceDiff=pow((newProfile['variance']-existingProfile['avgLength']),2)
		avgArticleDiff=pow((newProfile['articleIndex']-existingProfile['articleIndex']),2)
		prepIndexDiff=pow((newProfile['prepIndex']-existingProfile['prepIndex']),2)
		ppIndexDiff=pow((newProfile['ppIndex']-existingProfile['ppIndex']),2)
		commaIndexDiff=pow((newProfile['commaIndex']-existingProfile['commaIndex']),2)
		distance=math.sqrt(avgLengthDiff+avgConjDiff+commaIndexDiff+ppIndexDiff+prepIndexDiff)
		return distance

	def getClass(self, kNeighbours):
		authorDict=dict()
		authorDict['Joyce']=0
		authorDict['Dikens']=0
		for author in kNeighbours:
			authorDict[author]+=1
		if authorDict['Joyce']>authorDict['Dikens']:
			return 'Joyce'
		else:
			return 'Dikens'

knn=KNN(5)
p=profiler.Profiler()

directory='testData/Dikens'
for root, dirs, files in os.walk(directory):
	for myfile in files:
		if myfile.endswith(".txt"):
			fullPath=os.path.join(root,myfile)
			newProfile=ast.literal_eval(str(p.getProfile(fullPath,'Dikens')))
			knn.classify(newProfile)

directory='testData/Joyce'
for root, dirs, files in os.walk(directory):
	for myfile in files:
		if myfile.endswith(".txt"):
			fullPath=os.path.join(root,myfile)
			newProfile=ast.literal_eval(str(p.getProfile(fullPath,'Joyce')))
			knn.classify(newProfile)
