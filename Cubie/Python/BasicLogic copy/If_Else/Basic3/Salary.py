def calculate_tax():
    salary = float(input("Enter your salary: "))

    if salary <= 3000:
        tax = 0
    elif salary <= 4000:
        tax = 100
    elif salary <= 8000:
        tax = 0.06 * salary
    elif salary < 20000:
        tax = 0.10 * salary
    else:  # salary >= 20000
        tax = 0.16 * salary

    print(f"Salary: {salary:.2f}")
    print(f"Tax: {tax:.2f}")

calculate_tax()
