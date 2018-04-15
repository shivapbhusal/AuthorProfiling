'''
Implementation of K-Nearest Neighbour classifier
'''
import ast
import math

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
		neighbourClass=[]
		for i in range(self.K):
			neighbourClass.append(allDistances[keys[i]])
		print(neighbourClass)
			
	def getEuclidianDistance(self,newProfile, existingProfile):
		avgLengthDiff=pow((newProfile['avgLength']-existingProfile['avgLength']),2)
		varianceDiff=pow((newProfile['variance']-existingProfile['avgLength']),2)
		distance=math.sqrt(avgLengthDiff+varianceDiff)
		return distance

knn=KNN(5)
newProfile=dict()
newProfile['avgLength']=29.096153846153847
newProfile['variance']=7.133421400264201
print(knn.classify(newProfile))
