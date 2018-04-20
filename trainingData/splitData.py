'''
Read first 300 lines and write the content in a separate file. 

Generates separate files for the first 300 lines. 

'''
import os

textFilePath='Chekhov/witch_and_other_stories.txt'
lineCount=os.system('wc -l'+' '+textFilePath)

file=open(textFilePath)
start=0
end=300
newFilePath='Chekhov/witch_and_other_stories/'+str(start)+'-'+str(end)+'.txt'
try:
	for lines in file:
		newFile=open(newFilePath,'a')
		newFile.write(lines)
		start=start+1
		if start%300==0:
			end=end+300
			newFilePath='Chekhov/witch_and_other_stories/'+str(start)+'-'+str(end)+'.txt'
except UnicodeDecodeError:
	print("UnicodeDecodeError detected")


file.close()
