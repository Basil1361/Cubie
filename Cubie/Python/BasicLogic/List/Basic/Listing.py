# append is used for adding items
# push is for js / ts

a=[2,3,-5,12,54,0]
b=[5,-13,9,6,-8,67]
result = [] 

def appending():
    for i in range(6):
        formula = a[i]+b[i]
        result.append(formula)
    print(result)

appending()