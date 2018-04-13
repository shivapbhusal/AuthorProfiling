'''
Parses the given text file. 

'''

class Parser:
	def __init(self):
		print("A parser object created")

	def readTextFile(self, textFilePath):
		f=open(textFilePath)
		for lines in f:
			print(lines)

p=Parser()
p.readTextFile('../testData/Dikens/greatExpectations.txt')
