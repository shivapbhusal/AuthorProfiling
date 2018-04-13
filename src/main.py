'''
Main file. 
'''

import profiler as profiler
import os

def main():
	p=profiler.Profiler()
	lineCount=os.system('wc -l trainingData/Dikens/DavidCopperfield.txt')
	print(os.system('wc -l trainingData/Dikens/DavidCopperfield.txt'))
	print(lineCount)
	N=0
	while (N<=lineCount):
		trainingPortion=os.system('tail - '+str(lineCount-N)+' |'+ 'head -300 ' +'trainingData/Dikens/DavidCopperfield.txt')
		print(trainingPortion)
		N=N+300

	print(p.getProfile('trainingData/Dikens/DavidCopperfield.txt','Dikens'))
	#print(p.getProfile('trainingData/Chekhov/stories.txt','Chekhov'))

if __name__ == "__main__":
    main()