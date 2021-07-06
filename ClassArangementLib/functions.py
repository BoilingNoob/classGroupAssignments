import hashlib as crypt
import math

def findFactors(num):
    factors = []
    for i in range(1,num):
        if(num % i == 0):
            factors.append(i)
    return factors[1:]
def determinePossibleOrganizations(numberOfGroups,NumberOfObjects):
    #m = numberOfGroups       n = NumberOfObjects
    waysToAssort = math.factorial(numberOfGroups * NumberOfObjects) 
    waysToAssort /= (math.pow(math.factorial(NumberOfObjects),numberOfGroups) * math.factorial(numberOfGroups))
    return waysToAssort
class studentGroupDay:
    studentDict = {}
    numberOfStudents = 0
    numberOfGroups = 0
    studentGroupDict = {}


class situation:
    studentDict = {}
    numberOfStudents = 0
    numberOfGroups = 0
    studentGroupPlaylist = []

    def __init__(self,studentDict,numberOfGroups):
        self.studentDict = studentDict
        self.numberOfStudents = len(studentDict)
        self.numberOfGroups = numberOfGroups

    def determinePossibleOrganizations(self,numberOfGroups,NumberOfObjects):
        #m = numberOfGroups       n = NumberOfObjects
        waysToAssort = math.factorial(numberOfGroups * NumberOfObjects) 
        waysToAssort /= (math.pow(math.factorial(NumberOfObjects),numberOfGroups) * math.factorial(numberOfGroups))
        return waysToAssort
