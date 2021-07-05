def findFactors(num):
    factors = []
    for i in range(1,num):
        if(num % i == 0):
            factors.append(i)
    
    return factors[1:]

print(15,findFactors(15))
print(12345678,findFactors(12345678))