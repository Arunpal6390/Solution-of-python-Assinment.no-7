'''
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''

print("1. Yellow - Monday")
print("2. Blue - Tuesday")
print("3.Orange - Wednesday")
print("4.White - Thursday")
print("5.Black - Friday")
print("6.Red - Saturday")
print("7.All other colours - Sunday")
col=input("Enter your favorite colour name: ")
l1=["Yellow","Blue",".Orange","White","Black","Red"]
for colour in l1:
    if colour in col:
        c=colour
        break
else:
    c = "other"
match c:
    case "Yellow":
         print ("Monday")
    case "Blue":
         print("Tuesday")
    case "Orange":
         print("Wednesday")
    case "White":
         print("Thursday")
    case "Black":
         print("Friday")
    case "Red":
         print("Saturday")
    case "other colours":
         print("Sunday")
print()
