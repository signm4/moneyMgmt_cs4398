import numpy as np

def getIncome(userName):
    fileName = userName + ".txt"
    try:
        myFile = open(fileName, "r")
    except:
        line = 0
    fileLines = myFile.readlines()
    try:
        line = fileLines[0]
    except:
        line = 0
    incomeGained = 0
    incomeGained += float(line)
    return incomeGained

def getExpenses(userName):
    fileName = userName + ".txt"
    try:
        myFile = open(fileName, "r")
    except:
        return 0
    fileLines = myFile.readlines()
    try:
        line = fileLines[1]
    except:
        return 0
    expenses = 0
    expenses += float(line)
    return expenses

def addItem(userName, price, interval):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    incomeGained = getIncome(userName)

    expenses = getExpenses(userName)

    # The code below gets the current price of our expenses.
    myFile = open(fileName, "r")
    fileLines = myFile.readlines()
    try:
        line = fileLines[2]
    except:
        line = 0
    totalCost = 0
    totalCost += float(line)
    interval = (interval.upper())
    price = float(price)

    # I multiply the price to set it to yearly standards.
    if(interval == "MONTHLY"):
        price = price*12
    elif(interval == "WEEKLY"):
        price = price*52
    elif(interval == "DAILY"):
        price = price*365

    totalCost += price

    if(price > 0):
        incomeGained += price
    else:
        expenses += price

    myFile = open(fileName, "w")
    incomeGained = str(incomeGained)
    expenses = str(expenses)
    totalCost = str(totalCost)
    myFile.write(incomeGained + "\n")
    myFile.write(expenses + "\n")
    myFile.write(totalCost + "\n\n")

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

def printHelpMenu():
    print("\n\nHere's a list of all the available commands:\n")
    print("Type \"H\", or \"HELP\" to see this menu again.")
    print("Type \"Q\" or \"QUIT\" to quit the program.")
    print("Type \"P\" or \"PRINT\" to print the list.")
    print("Type \"D\" or \"DELETE\" to delete an item from the list.")
    print("Type \"INC\" or \"INCOME\" to add an income.")
    print("Type \"EXP\" or \"EXPENSE\" to add an expense.")
    print("Type \"INCNUM\" or \"INCOMENUMBER\" to get the total income.")
    print("Type \"EXPNUM\" or \"EXPENSESNUMBER\" to get the total expenses.")
    print("")   # This is just for an extra endline at the end of my menu.

def deleteAllData(userName):
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
    except:
        myFile = open(fileName, "x")

    myFile = open(fileName, "w")
    myFile.write("")
