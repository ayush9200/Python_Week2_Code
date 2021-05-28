# DATETIME.PY 3.Write a Python program to display the current date and time.

from datetime import datetime
def main():
    printCurrentDateTime()

def printCurrentDateTime():
    date = datetime.now().date()
    time = datetime.now().time()
    time = time.strftime("%H:%M:%S")
    print(f'Today date is {date} and time is {time}')

main()
#this is main method for this module