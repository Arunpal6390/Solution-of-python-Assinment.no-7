'''
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number
'''
x=int(input("Enter any number: "))
match x:
    case x if  x%2 == 0 :
        print("Given number is even")
        print("Saurabh Shukla")
    case x if x<0 and x%2==1:
        print("Given number is negative odd number")
        print("print Prateek Jain")
    case x if x>0 and x%2==1:
        print("Given number is positive odd number")
        print("Aditya Choudhary ")