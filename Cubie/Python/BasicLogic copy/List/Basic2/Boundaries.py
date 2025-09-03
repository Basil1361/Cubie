data = [3, 12, 10, 1, 7, 9, 7, 4, 3, 11]


def smallest(): 
    k = data[0]
    for i in range(len(data)):
        if data[i] < k:
            k = data[i]
    print(k, "is the smallest value")
    

def largest():
    k = data[0]
    for i in range(len(data)):
        if data[i] > k:
            k = data[i]
    print(k, "is the largest value")

smallest()
largest()

# # alternative: using min and max 
# min_value = min(data)
# max_value = max(data)
# min_idx = data.index(min_value)  # first occurrence
# max_idx = data.index(max_value)
# print(f"min {min_value} at index {min_idx}, max {max_value} at index {max_idx}")
