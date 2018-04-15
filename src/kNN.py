'''
Implementation of K-Nearest Neighbour classifier
'''
import ast
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
		print(kNeighbours)
		print(self.getClass(kNeighbours))
			
	def getEuclidianDistance(self,newProfile, existingProfile):
		avgLengthDiff=pow((newProfile['avgLength']-existingProfile['avgLength']),2)
		varianceDiff=pow((newProfile['variance']-existingProfile['avgLength']),2)
		distance=math.sqrt(avgLengthDiff+varianceDiff)
		return distance

	def getClass(self, kNeighbours):
		authorDict=dict()
		for author in kNeighbours:
			if author not in authorDict:
				authorDict[author]=1
			else:
				authorDict[author]+=1
		print(authorDict)
		if authorDict['Joyce']==5:
			return 'Joyce'
		elif authorDict['Dikens']==5:
			return 'Dikens'
		else:
			if authorDict['Joyce']>authorDict['Dikens']:
				return 'Joyce'
			else:
				return 'Dikens'

knn=KNN(5)
p=profiler.Profiler()
directory='testData/Joyce/test4.txt'
newProfile=ast.literal_eval(str(p.getProfile(directory,'Joyce')))
knn.classify(newProfile)

#print(knn.classify(newProfile))
