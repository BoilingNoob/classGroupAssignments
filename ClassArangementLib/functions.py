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

    def __init__(self,studentDict,numberOfGroups,studentGroupDict):
        self.studentDict = studentDict
        self.numberOfStudents = len(studentDict)
        self.numberOfGroups = numberOfGroups
        self.studentGroupDict = studentGroupDict


class situation:
    studentDict = {}
    numberOfStudents = 0
    numberOfGroups = 0
    studentGroupPlaylist = []

    def __init__(self,studentDict,numberOfGroups):
        self.studentDict = studentDict
        self.numberOfStudents = len(studentDict)
        self.numberOfGroups = numberOfGroups

    def determinePossibleOrganizations(self):
        #m = self.numberOfGroups       n = self.numberOfStudents
        waysToAssort = math.factorial(self.numberOfGroups * self.numberOfStudents) 
        waysToAssort /= (math.pow(math.factorial(self.numberOfStudents),self.numberOfGroups) * math.factorial(self.numberOfGroups))
        return waysToAssort

    def organizeGroups(self):
        for i in range(determinePossibleOrganizations()):
            
            studentGroupDict = {}#generate day groups


            temp = studentGroupDay(self.studentDict,self.numberOfGroups,studentGroupDict)
            self.studentGroupPlaylist.append(temp)