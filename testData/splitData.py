'''
Read first 300 lines and write the content in a separate file. 

Generates separate files for the first 300 lines. 

'''
import os

textFilePath='portrait_of_the_artist_as_young_man.txt'
lineCount=os.system('wc -l'+' '+textFilePath)

file=open(textFilePath)
start=6900
end=7200
newFilePath='Joyce/'+str(start)+'-'+str(end)+'portrait.txt'
for lines in file:
	try:
		newFile=open(newFilePath,'a')
		newFile.write(lines)
		start=start+1
		if start%300==0:
			end=end+300
			newFilePath='Joyce/'+str(start)+'-'+str(end)+'.txt'
	except UnicodeDecodeError:
		continue


file.close()
