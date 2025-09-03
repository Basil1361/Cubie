# Write the function check(data, dtype) that can check if the type of all the items in data equals the dtype or not.

# The function should return Trueor False.

# Now write the program to use the function and check list a given below with str or int data type.

# There are various data types you can use such as str for String and int for Integer.
# Use type(data) to return the data type of the item/elements.

data = [2,3,"h",3,2,34,"h","h",-34]

def check(data,dtype):
    for i in range(len(data)):
        if type(data[i]) == dtype:
            print("Index", i, "shares the same number type")
        else:
            print("Index", i, "doesn't share the same type", "it's a", type(i))
            
            
check(data,type(data[0]))