# During the weekends, you went to shopping with your family. 
# You want to know how much you have spent. Create a program to calculate how much you have spent.
# First, create the list amounts for the items that you bought (4 items).
# Then, create the list prices for the items (in the same index as the amounts).
# Calculate the sum of the items in amounts * prices.
# Remember to multiply the values of the list according to the indexes 
# and you will need a loop to run through the list.

items = ["apples", "bananas", "carrots", "cookies"]
prices = [5, 6, 7, 4]
quantity = [5, 10, 5, 8]

def Formula(): 
    total = 0 
    for i in range(len(items)):
        sum = prices[i]*quantity[i]
        total += sum
    print("The total amount is RM", total)
    
Formula()
    