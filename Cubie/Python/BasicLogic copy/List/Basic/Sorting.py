import random
data = []

for _ in range(5):
    data.append(random.randint(-50, 50))

print("Original list:", data)

for i in range(len(data)):
    k = i  # assume current index is smallest
    for j in range(i + 1, len(data)):
        if data[j] < data[k]:  # find smaller value
            k = j
    data[i], data[k] = data[k], data[i]  # swap

print("Sorted list:", data)
