# DATETIME.PY 3.Write a Python program to reverse name taken as input from user.

def printReversedName():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    full_name = first_name + " " + last_name
    reversed_name = ""

    # Executing loop in reversed
    for count in range(len(full_name),0,-1):
        reversed_name = reversed_name + full_name[count-1]
    print(reversed_name)
