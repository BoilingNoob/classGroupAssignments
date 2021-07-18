from os import replace
import hashlib as crypt
import math
from ClassArangementLib import functions as classFuncs
import random as rand

listOfStudents = classFuncs.getStudentList('names.txt')
randomizedList = classFuncs.generateGroupRawListRandom(listOfStudents)


print(listOfStudents)
print(randomizedList)