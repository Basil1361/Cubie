data = [ 2,3,4,5,6,7,2,-2,3, -5,12,34,23,1,2,1,3,4,5 ] 

def defined():
    s = int(input("Enter: "))
    t = int(input("Enter: "))
    for i in range(len(data)):
        if data[i] == s:
            data[i] = t
    print(data)
            
            
defined()

# data[i] is the values
# i is the index! 

