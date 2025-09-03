listing = [1,2,3,4,5]

def value():
    count = listing[0]
    for i in listing:
        if i > count:
            count = i
    return count

print(value())
