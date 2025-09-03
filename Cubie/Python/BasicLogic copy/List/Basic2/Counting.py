a = [2,3,'h',3,2,34,'h','h',-34]
b = [2,'h']



def countinga():
    x = input("Enter Something for list a: ")
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
        else:
            continue
    print("There is",count,x,"'s","in list a")
    


def countingb():
    x = int(input("Enter Something for list b: "))
    count = 0
    for i in range(len(b)):
        if b[i] == x:
            count += 1
        else:
            continue
    print("There is",count,x,"'s","in list b")
    
countinga()
countingb()
