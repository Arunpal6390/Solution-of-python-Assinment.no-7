'''
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
'''
print("1.isosceles triangle") # when any two length of side are equal then it is called isosceles triangle.
print("2.right triangle")   # when any square of one side is equal to sum of square remains two side.
print("3.equilateral triangle") # when all length of side are equal to each other .
print("4.Exit")
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        l1 = float(input("Enter length of triangle side.1: "))
        l2 = float(input("Enter length of triangle side.2: "))
        l3 = float(input("Enter length of triangle side.3: "))
        if l1 == l2 or l1 == l3:
            print("Given length of triangle is isosceles")
        elif l2 == l3:
            print("Given length of triangle is isosceles")
        else:
            print("Given length of triangle is not isosceles")
    case 2:
       l1 = float(input("Enter length of triangle side.1: "))
       l2 = float(input("Enter length of triangle side.2: "))
       l3 = float(input("Enter length of triangle side.3: "))
       if l1*l1 == l2*l2 + l3*l3 or l2*l2 == l1*l1 + l3*l3:     # formula(a^2=b^2+c^2)
           print("Given length of triangle is right triangle")
       elif l3**2 == l1**2 + l2**2:
           print("Given length of triangle is right triangle")
       else:
           print("Given length of triangle is not right triangle")
    case 3:
          l1 = float(input("Enter length of triangle side.1: "))
          l2 = float(input("Enter length of triangle side.2: "))
          l3 = float(input("Enter length of triangle side.3: "))
          if l1 == l2 == l3:
              print("Given length of triangle is equilateral triangle")
          else:
              print("Given length of triangle is not equilateral triangle")
    case 4:
        exit()
    case _:
        print("Invalied choice")


