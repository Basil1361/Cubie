import random

s = []
for _ in range(30): 
    s.append(random.randint(0, 31))

print("List s:", s)

for index in range(len(s)): 
    if index >= s[index]:
        print(f"Index: {index}, Value: {s[index]}")
        
        
