from os import replace
import hashlib as crypt
import math
from ClassArangementLib import functions as classFuncs


studentDict = {}

with open('names.txt','r') as reader:
    listOfStudents = reader.readlines()

for i in range(len(listOfStudents)):
    listOfStudents[i] = listOfStudents[i].replace('\n','')
    hashed = (crypt.md5(listOfStudents[i].encode())).hexdigest()
    studentDict[hashed]=listOfStudents[i]


plusOne = classFuncs.findFactors(len(studentDict)+1)
print(" Plus One factors: ",plusOne)
minusOne = classFuncs.findFactors(len(studentDict)-1)
print("Minus One factors: ",minusOne)
plusTwo = classFuncs.findFactors(len(studentDict)+2)
print(" Plus Two factors: ",plusTwo)
minusTwo = classFuncs.findFactors(len(studentDict)-2)
print("Minus Two factors: ",minusTwo)
convinientFactors = classFuncs.findFactors(len(studentDict))
print(" Nice Group Sizes: ",convinientFactors)


#for hash,student in studentDict.items():
#    print(student)