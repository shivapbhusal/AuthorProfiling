'''
Main file. 
'''

import profiler as profiler
import os

def main():
	p=profiler.Profiler()
	directory='trainingData/Dikens/DavidCopperfield'
	for root, dirs, files in os.walk(directory):
		for myfile in files:
			if myfile.endswith(".txt"):
				fullPath=os.path.join(root,myfile)
				print(p.getProfile(fullPath,'Dikens'))

	directory='trainingData/Joyce/Ulysses_Dubliners'
	for root, dirs, files in os.walk(directory):
		for myfile in files:
			if myfile.endswith(".txt"):
				fullPath=os.path.join(root,myfile)
				print(p.getProfile(fullPath,'Ulysses'))

	#print(p.getProfile('trainingData/Chekhov/stories.txt','Chekhov'))

if __name__ == "__main__":
    main()