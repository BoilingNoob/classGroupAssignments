from os import replace
import hashlib as crypt
import math
#import ClassArangementLib as classFuncs
import random as rand
from ClassArangementLib import functions as classFuncs

listOfStudents = classFuncs.getStudentList('names.txt')
randomizedList = classFuncs.generateGroupRawListRandom(listOfStudents)

def makeGroups(numberOfGroups,RandomizedStudentList):
    listOfGroups = []
    numberOfStudents = len(RandomizedStudentList)
    ExtraStudents = numberOfStudents % numberOfGroups
    studentsPerGroupEven = (numberOfStudents - (ExtraStudents) )/numberOfGroups
    mutStudentList = RandomizedStudentList
    

    for i in range(0,numberOfGroups):
        temproup = []
        for j in range(0,studentsPerGroupEven):
            temproup.append(mutStudentList.pop())
        if(i < ExtraStudents):
            temproup.append(mutStudentList.pop())

        listOfGroups.append(temproup)

    return listOfGroups

"""
print(listOfStudents)
print(randomizedList)
"""


groups = makeGroups(4,randomizedList)
print(groups[0])