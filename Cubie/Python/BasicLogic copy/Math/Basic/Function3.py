def Summation(n , k):
    result = 0
    for i in range(n, k + 1): 
        result += i
    return result

s1 = Summation(5,23)
s2 = Summation(12,23)
s3 = Summation(5,12)

print((s1 + s2) // s3)
# // means integer division