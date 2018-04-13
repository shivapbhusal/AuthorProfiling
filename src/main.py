'''
Main file. 
'''

import profiler as profiler

def main():
	p=profiler.Profiler()
	print(p.getProfile('testData/Dikens/greatExpectations.txt','Dikens'))
	print(p.getProfile('testData/Chekhov/stories.txt','Chekhov'))

if __name__ == "__main__":
    main()