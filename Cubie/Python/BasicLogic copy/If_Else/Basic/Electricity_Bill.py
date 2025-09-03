def Electric():
    while True:
        try:
            value = int(input("Enter your amount: "))
            break
        except ValueError:
            print("The value is not valid")
    name = input("Enter your name: ")
    return value, name

def compute_raw_bill(units):
    # Free up to 50 units
    if units <= 50:
        return 0.0

    bill = 0.0

    # 51–200 @ RM1.3
    if units <= 200:
        return (units - 50) * 1.3
    bill += 150 * 1.3

    # 201–400 @ RM1.6
    if units <= 400:
        return bill + (units - 200) * 1.6
    bill += 200 * 1.6

    # 401–600 @ RM1.9
    if units <= 600:
        return bill + (units - 400) * 1.9
    bill += 200 * 1.9

    # >600 @ RM2.2
    return bill + (units - 600) * 2.2

def Payment(amt, name):
    raw = compute_raw_bill(amt)

    # 5% discount if raw > 500, capped at RM50
    discount = 0.0
    if raw > 500:
        discount = min(raw * 0.05, 50)

    final_amount = raw - discount
    print(f"{name}, the electric bill is RM{final_amount:.2f}")
    return final_amount

# --- run it ---
value, Name = Electric()
Payment(value, Name)
