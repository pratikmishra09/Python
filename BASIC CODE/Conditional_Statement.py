# a=int(input("Enter Your Age:"))
# print(a)
# import time

day = int(input("Enter the day :"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
