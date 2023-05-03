import numpy as np

# Constructor with name
def addItem2(name, price, interval):

    myFile = open("storageFile.txt", "r")
    previousData = myFile.read()

    myFile = open("storageFile.txt", "w")
    myFile.write(previousData)
    myFile.write("Name: " + name + "\n")
    myFile.write("Price: " + price + "\n")
    myFile.write("Interval: " + interval + "\n")

# Constructor without name
def addItem1(price, interval):
    myFile = open("storageFile.txt", "r")
    previousData = myFile.read()

    myFile = open("storageFile.txt", "w")
    myFile.write(previousData)
    myFile.write("Price: " + price + "\n")
    myFile.write("Interval: " + interval + "\n")

def printList():
    myFile = open("storageFile.txt", "r")
    print(myFile.read())

def pop():
    myFile = open("storageFile.txt", "r")
    myString = myFile.read()
    # I find the first instance of the word "interval".
    myString = myString[myString.find("Interval:"):]
    if(myString.find("Name:") < myString.find("Price:") and myString.find("Name:") != -1):
        myString = myString[myString.find("Name:"):]
    else:
        myString = myString[myString.find("Price:"):]

    myFile = open("storageFile.txt", "w")
    myFile.write(myString)








'''def basePrice(item):
    if(item[2] == "daily"):
        return item[1]
    elif(item[2] == "weekly"):
        return item[1]/7
    elif(item[2] == "monthly"):
        return item[1]/30
    else:
        return item[1]/365
    
def dailyExpidentureCosts(myList):
    totalExpidentures = 0
    for index in myList:
        totalExpidentures += basePrice(index)
    return totalExpidentures

def printAverage(list):
    print("Please input either D, W, M, or Y to signify")
    print("if you want to know the Daily expenses, Weekly expenses, Monthly expenses, or Yearly expenses.")
    myChoice = input("Input: ")
    myChoice = myChoice.upper()
    if myChoice == 'D' or myChoice == "DAILY":
        print("$", dailyExpidentureCosts(list))
    elif myChoice == 'W' or myChoice == "WEEKLY":
        print("$", dailyExpidentureCosts(list)*7)
    elif myChoice == 'M' or myChoice == "MONTHLY":
        print("$", dailyExpidentureCosts(list)*30)
    elif myChoice == 'Y' or myChoice == "YEARLY":
        print("$", dailyExpidentureCosts(list)*365)
    else:
        print("ERROR: COMMAND NOT RECOGNIZED")

def printHelpMenu():
    print("\n\nHere's a list of all the available commands:\n")
    print("Type \"H\", or \"HELP\" to see this menu again.")
    print("Type \"E\" or \"EXIT\" to exit the program.")
    print("Type \"P\", \"PRINT\", or \"PRINTLIST\" to print the list.")
    print("Type \"N\", \"NEW\", or \"NEWITEM\" to add a new item to the list.")
    print("Type \"PA\" or \"PRINTAVERAGE\" to print the average costs.")
    print("Type \"D\", \"DELETE\", or \"DELETEITEM\" to delete an item from the list.")
    print("")   # This is just for an extra endline at the end of my menu.

def deleteItem(myList):
    print("\nChoose which item to delete: ")
    printList(myList)
    print() # This is just for that one extra line in the console output.

    myChoice = input("Input: ")
    if myChoice.isdigit():
        myChoice = int(myChoice)
        myList.pop(myChoice-1)
        print("New List:")
        printList(myList)
    else:
        print("ERROR: INVALID INPUT")
    
    return myList

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
'''