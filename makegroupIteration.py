from os import replace
import hashlib as crypt
import math
from ClassArangementLib import functions as classFuncs
import random as rand

def generateGroupRawList(classList):
    groupList = []
    classListRandomized = []
    classListMutable = classList
    rand.seed()
    for i in range(0,len(classList)):
        randInt = rand.randrange(0,len(classListMutable))
        groupList.append(classListMutable.pop(randInt))
    
    return groupList


listOfStudents = classFuncs.getStudentList('names.txt')
print(listOfStudents)

randomizedList = generateGroupRawList(listOfStudents)

print(randomizedList)

