# Create a list of numbers, maximum 10 items.

# Now for each item find the square of the item and put it in a new list named squared.

# Now print both original and new lists.

# Review task 3 for the command to add items into a new list.

listing = [1,2,3,4,5,6,7,8,9,10]
sqlisting = []

def squared():
    for i in range(10):
        formula = (listing[i])**2
        sqlisting.append(formula)
    print("Initial list: ",listing)
    print("Squared list: ",sqlisting)
        
squared()
