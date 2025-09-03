import random

# Create 2 empty lists
data1 = []
data2 = []

# Fill both lists with 20 random integers between 10 and 30
for _ in range(20):
    data1.append(random.randint(10, 30))
    data2.append(random.randint(10, 30))

def find_common(list1, list2):
    # Use nested loop to check items from both lists
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

# Print the result
result = find_common(data1, data2)
print(f"Common item found: {result}")

# Optional: print the lists to see the data
print(f"Data1: {data1}")
print(f"Data2: {data2}")
