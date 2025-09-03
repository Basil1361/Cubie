# Step 1: Get input
data = int(input("Enter a number: "))

# Step 2: Store original value
temp = data

# Step 3: Reverse number
reverse = 0

while data > 0:
    last_dig = data % 10
    reverse = reverse * 10 + last_dig
    data = data // 10

# Step 4: Check palindrome
if reverse == temp:
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")