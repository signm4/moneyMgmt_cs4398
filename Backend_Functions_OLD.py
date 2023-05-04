import numpy as np

def addItem(userName, price, interval):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    # The code below gets the current price of our expenses.
    myFile = open(fileName, "r")
    fileLines = myFile.readlines()
    totalCost = 0
    for line in fileLines:
        if line.find("Price: ") != -1:
            totalCost += float(line[7:])
    interval = (interval.upper())
    price = float(price)
    # I multiply the price to set it to yearly standards.
    if(interval == "YEARLY"):
        totalCost = totalCost + price
    elif(interval == "MONTHLY"):
        totalCost = totalCost + price*12
    elif(interval == "WEEKLY"):
        totalCost = totalCost + price*52
    elif(interval == "DAILY"):
        totalCost = totalCost + price*365

    myFile = open(fileName, "w")
    totalCost = str(totalCost)
    myFile.write("Price: " + totalCost + "\n")
    myFile.write("Interval: YEARLY\n\n")

def addIncome(userName, price, interval):
    addItem(userName, price, interval)

def addExpense(userName, price, interval):
    price = float(price)
    price *= -1
    price = str(price)
    addItem(userName, price, interval)

def printList(userName):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    myFile = open(fileName, "r")
    print(myFile.read())

def pop(userName):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    myFile = open(fileName, "r")
    myString = myFile.read()
    # I find the first instance of the word "interval".
    myString = myString[myString.find("Interval:"):]
    if(myString.find("Name:") < myString.find("Price:") and myString.find("Name:") != -1):
        myString = myString[myString.find("Name:"):]
    else:
        myString = myString[myString.find("Price:"):]

    myFile = open(fileName, "w")
    myFile.write(myString)

def printHelpMenu():
    print("\n\nHere's a list of all the available commands:\n")
    print("Type \"H\", or \"HELP\" to see this menu again.")
    print("Type \"Q\" or \"QUIT\" to quit the program.")
    print("Type \"P\" or \"PRINT\" to print the list.")
    print("Type \"D\" or \"DELETE\" to delete an item from the list.")
    print("Type \"DA\" or \"DELETEALL\" to delete all items from the list.")
    print("Type \"INC\" or \"INCOME\" to add an income.")
    print("Type \"EXP\" or \"EXPENSE\" to add an expense.")
    print("Type \"DA\" or \"DELETEALL\" to delete all items from the list.")
    print("")   # This is just for an extra endline at the end of my menu.

def deleteAllData(userName):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    myFile = open(fileName, "w")
    myFile.write("")

def getAverage(userName):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    myFile = open(fileName, "r")
    fileLines = myFile.readlines()
    totalCost = 0
    totalNumberOfItems = 0
    for line in fileLines:
        if line.find("Price: ") != -1:
            totalNumberOfItems += 1
            totalCost += float(line[7:])
    return totalCost/totalNumberOfItems














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