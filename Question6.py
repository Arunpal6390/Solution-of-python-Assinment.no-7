'''
6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement
'''
string=input("Enter any string: ")
string.strip()
match string:
    case string if ' ' in string:
        print("multiword string")
    case string if ' ' not in string:
        print("single word string")
    case _:
        print("Invalied")
