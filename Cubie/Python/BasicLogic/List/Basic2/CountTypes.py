# Now, modify the function to read 2 lists as parameters.

# the first one is data that contains different items.
# the second one is a list of different data types.

# Now the function should count the number of each data type from the second list found in the first one and print the count result, and does it for all the items in dtype. For example:

# a = [2,3,"h",3,2.0,3.44,"h","h",-34]
# tp = [str,int,float]
# Output:

# Count:  3 # because there's 3 tp[0] found in list a
# Count:  4 # 4 tp[1] found in list a
# Count:  2 # and 2 tp[2] found in list a

data = [2,3,"h",3,2.0,3.44,"h","h",-34]

def check(data, dtype):
    for data_type in dtype:
        count = 0
        for i in range(len(data)):
            if type(data[i]) == data_type:
                count += 1
        print("Count: ", count)

tp = [str, int, float]
check(data, tp)