# a  = [ 12,13,-23,0.34, 2.4 , -345, -13, 15, 2.0 ]
# Print the items that their index is odd or dividable by 3.

# Here, you may need to check for the indexes instead of the values from the list.

a = [12,13,-23,0.34,2.4,-345,-13,15,2.0 ]
b = []

def condition():
    for i in range(len(a)):
        if a[i] % 3 == 0 or a[i] % 2 == 1:
            b.append(i)
        else:
            continue
    print(b)
condition()

