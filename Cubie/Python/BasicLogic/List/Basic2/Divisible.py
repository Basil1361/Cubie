test = [2,3,4,7,11,17,31]
value = 24

def trying(): 
    for i in range(len(test)):
        if value % test[i] == 0: 
            print(value,"is divisible by", test[i])
        else:
            continue
        
trying()