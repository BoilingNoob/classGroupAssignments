#Jaccard Index = (the number in both sets) / (the number in either set) * 100
#will go O((n+1) /2) as each group needs to be measure against eachother
#source https://www.statisticshowto.com/jaccard-index/
from os import replace
import hashlib as crypt
import math
from ClassArangementLib import functions as classFuncs

debugging = False #True False  #if(debugging):print("")

studentDict = {}

with open('names.txt','r') as reader:
    listOfStudents = reader.readlines()

if(debugging):print("got data")

for i in range(len(listOfStudents)):
    listOfStudents[i] = listOfStudents[i].replace('\n','')
    hashed = (crypt.md5(listOfStudents[i].encode())).hexdigest()
    studentDict[hashed]=listOfStudents[i]

if(debugging):print("made dictionary")

listA = [1,2,3,4,5]
listA = classFuncs.genList(listA,listOfStudents)
if(debugging):print("made listA",listA)
listB = [1,7,8,9,0]
listB = classFuncs.genList(listB,listOfStudents)
if(debugging):print("made listB",listB)

similarity = classFuncs.calcJaccard(listA,listB)

print(similarity)
