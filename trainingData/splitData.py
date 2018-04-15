'''
Read first 300 lines and write the content in a separate file. 

Generates separate files for the first 300 lines. 

'''
import os

textFilePath='Dikens/DavidCopperField.txt'
lineCount=os.system('wc -l'+' '+textFilePath)

file=open(textFilePath)
start=0
end=300
newFilePath='Dikens/'+str(start)+'-'+str(end)+'.txt'
for lines in file:
	newFile=open(newFilePath,'a')
	newFile.write(lines)
	start=start+1
	if start%300==0:
		end=end+300
		newFilePath='Dikens/DavidCopperField/'+str(start)+'-'+str(end)+'.txt'

file.close()
