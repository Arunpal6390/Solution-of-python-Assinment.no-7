'''2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
'''

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice:  "))
match choice:
    case 1:
        number1=float(input("Enter a first number: "))
        number2=float(input("Enter a second number: "))
        result=number1+number2
        print("Addition of two number is: ",result)
    case 2:
        number1 = float(input("Enter a first number: "))
        number2 = float(input("Enter a second number: "))
        result = number1 - number2
        print("Subtraction of two number is: ", result)
    case 3:
        number1 = float(input("Enter a first number: "))
        number2 = float(input("Enter a second number: "))
        result = number1 * number2
        print("Multiplication of two number is: ", result)
    case 4:
        number1 = float(input("Enter a first number: "))
        number2 = float(input("Enter a second number: "))
        result = number1 / number2
        print("Division of two number is: ", result)
print()
