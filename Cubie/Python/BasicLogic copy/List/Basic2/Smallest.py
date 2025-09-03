data = [9,3,6,89,2]

def smallest(): 
    k = data[0]
    for i in range(len(data)):
        if data[i] < k:
            k = data[i]
    print(k, "is the smallest value")
    
smallest()