from os import replace
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

studentDict = {}

with open('names.txt','r') as reader:
    listOfStudents = reader.readlines()

for i in range(len(listOfStudents)):
    listOfStudents[i] = listOfStudents[i].replace('\n','')
    hashed = (crypt.md5(listOfStudents[i].encode())).hexdigest()
    studentDict[hashed]=listOfStudents[i]

convinientFactors = findFactors(len(studentDict))
if(convinientFactors == []):
    plusOne = findFactors(len(studentDict)+1)
    print(" Plus One factors: ",plusOne)
    minusOne = findFactors(len(studentDict)-1)
    print("Minus One factors: ",minusOne)
    plusTwo = findFactors(len(studentDict)+2)
    print(" Plus Two factors: ",plusTwo)
    minusTwo = findFactors(len(studentDict)-2)
    print("Minus Two factors: ",minusTwo)



print(" Nice Group Sizes: ",convinientFactors)



#for hash,student in studentDict.items():
#    print(student)