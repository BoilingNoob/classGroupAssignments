def findFactors(num):
    factors = []
    for i in range(1,num):
        if(num % i == 0):
            factors.append(i)
    
    return factors[1:]

print(31,findFactors(31))

print([] == findFactors(31))