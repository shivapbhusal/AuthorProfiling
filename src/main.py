'''
Main file. 
'''

import profiler as profiler
import os

def main():
	p=profiler.Profiler()
	directory='trainingData/Dikens/DavidCopperfield'
	outputFile="results/authorProfiles.txt"
	with open(outputFile, 'w') as textFile:
		for root, dirs, files in os.walk(directory):
			for myfile in files:
				if myfile.endswith(".txt"):
					fullPath=os.path.join(root,myfile)
					resultForDikens = p.getProfile(fullPath,'Dikens')
					textFile.write(str(resultForDikens)+'\n')				
	textFile.close


	directory='trainingData/Joyce/Ulysses_Dubliners'
	with open(outputFile, 'a') as textFile:
		for root, dirs, files in os.walk(directory):
			for myfile in files:
				if myfile.endswith(".txt"):
					fullPath=os.path.join(root,myfile)
					resultForJoyce=p.getProfile(fullPath,'Joyce')
					textFile.write(str(resultForJoyce)+'\n')	
	textFile.close
	#print(p.getProfile('trainingData/Chekhov/stories.txt','Chekhov'))

if __name__ == "__main__":
    main()