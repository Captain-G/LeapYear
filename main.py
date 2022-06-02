# a leap year is any year that is divisible by 4
# except every year that is divisible by 100
# unless it is also divisible by 400

year = int(input("Enter the year that you want to test : "))
isLeap = True
if year % 4 == 0:
    isLeap = True
    if year % 100 == 0:
        isLeap = False
        if year % 400 == 0:
            isLeap = True

if isLeap is True:
    print("Leap")
else:
    print("NOT leap")