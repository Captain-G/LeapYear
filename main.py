# a leap year is any year that is divisible by 4
# except every year that is divisible by 100
# unless it is also divisible by 400

year = int(input("Enter the year that you want to test : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("IS a leap year.")
        else:
            print("NOT a leap year.")
    else:
        print("NOT a leap year.")
else:
    print("NOT a leap year.")
