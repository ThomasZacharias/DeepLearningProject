import os
import string
# def convertTXTFile(fileName, fileOutName):
os.chdir("/home/thomasz/Desktop/Thomas/DeepLearningProject/Language translator/language-style-transfer-master/data/English0-Hebrew1")
os.getcwd()
fileName = "language.test.0"
outputFile = "languageF.test.0"

ogFile = open(fileName, 'r')
newFile = open(outputFile, 'w+')

while True:
	char = ogFile.read(1)
	if not char:
		print("End of file")
		break
	if char == '\n':
		newFile.write('\n')
	elif char == ' ':
		newFile.write('\n')
	elif char in string.punctuation:
		continue
	else:
		newFile.write(char)
		newFile.write(' ')

newFile = open(outputFile, 'r')
lines = newFile.readlines()
newFile = open(outputFile, 'w+')
for line in lines:
	if line != '\n':
		newFile.write(line)