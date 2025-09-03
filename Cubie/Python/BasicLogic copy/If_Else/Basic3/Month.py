month1 = ['Apr', 'Jun', 'Sept', 'Nov']
month2 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']

def MonthChecking():
    month = input("Please enter a valid month, first three letters: ")
    if month in month1:
        print("The days are 30")
    elif month in month2:
        print("The days are 31")
    elif month == "Feb":
        year = int(input("Enter the year: "))
        if year % 4 == 0:
            print("The days are 29")
        else:
            print("The days are 28")
    else:
        print("Invalid Month")
        

MonthChecking()