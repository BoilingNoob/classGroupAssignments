from os import replace
import hashlib as crypt
import math
from ClassArangementLib import functions as classFuncs

def calc2JaccardVal(classItA,classItB):
    #take two iteratiosn of groups, compare each group of list1 to list2
    jaccardIndicies = []
    for groupA in range(0,len(classItA)):
        for groupB in range(0,len(classItB)):
            jaccardIndicies.append(classFuncs.calcJaccard(groupA,groupB))

    return jaccardIndicies


