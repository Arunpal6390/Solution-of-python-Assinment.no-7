'''
4. Write a program which takes users age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
'''
print("1.Kid.") # age below 10 years.
print("2.Teen.") # age below 20 years.
print("3.young.") # age below 40 years.
print("4.Experienced.") # age  below 60 years.
print("5.Senior Citizen.") # age above or equal 60 years.
age=int(input("Enter any age: "))
match age:
    case age if age < 10:
        print("Kild")
    case age if age<20:
        print("Teen")
    case age if age<40:
        print("Young")
    case age if age<60:
        print("Experienced")
    case age if age>60 or age==60:
        print("Senior Citizen")
    case _:
        print()