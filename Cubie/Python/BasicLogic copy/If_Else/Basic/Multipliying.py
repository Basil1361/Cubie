# Write a Python program which iterates the integers from 1 to 60. 
# For multiples of three print "Kido" instead of the number and for the multiples of five print "Code".
# For numbers which are multiples of both three and five print "KidoCode".

def checking(n):
    a = "Kido"
    b = "Code"
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(f"{i} = {a}")
        if i % 5 == 0:
            print(f"{i} = {b}")
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} = {a+b}")
        else:
            continue
    return(a,b)

checking(60)