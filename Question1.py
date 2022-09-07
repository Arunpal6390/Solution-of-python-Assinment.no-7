#1. Write a python script to display the number of days in a given month number.
print("January", "March", "May", "July", "August", "October", "December","April", "June", "September", "November","February")
x=input("Enter any month name:")
match x:
    case "January":
        print("Number of 31 days")
    case "February":
        print("Number of 28/29 days")
    case "March":
        print("Number of 31 days")
    case "April":
        print("Number of 30 days")
    case "May":
        print("Number of 31 days")
    case "June":
        print("Number of 30 days")
    case "July":
        print("Number of 31 days")
    case "August":
        print("Number of 31 days")
    case "September":
        print("Number of 30 days")
    case "October":
        print("NUmber of 31 days")
    case "November":
        print("Number of 30 days")
    case "December":
        print("Number of 31 days")
    print()

