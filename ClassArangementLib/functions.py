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

def calcJaccard(listA,listB):
    similarities = 0
    totalElements = 0
    mixedList = listA + listB
    uniqueSet = set(mixedList)

    for item in uniqueSet:
        if(item in listA and item in listB):
            similarities+=1
    
    totalElements = len(uniqueSet)

    return (similarities/totalElements) *100

def genList(list,studentList):
    for i in range(0,len(list)):
        list[i] = studentList[list[i]]
    return list

def getStudentList(textFile):
    with open(textFile,'r') as reader:
        listOfStudents = reader.readlines()
    return listOfStudents


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