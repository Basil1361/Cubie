def SumOfFactors13():
    count13 = 0
    for i in range(1,200+1):
        if i % 13 == 0:
            count13 += i
        else:
            continue
    return count13
    
def SumOfFactors17():
    count17 = 0
    for i in range(1,200+1):
        if i % 17 == 0:
            count17 += i
        else:
            continue
    return count17

print(SumOfFactors17() + SumOfFactors13())     
   