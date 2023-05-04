import numpy as np


# Returns the income as a float value
def getIncome(userName):
    # Sets filename to the current user and appends a .txt
    fileName = userName + ".txt"
    try:
        # tries to open this file in case it exists.
        myFile = open(fileName, "r")
    except:
        # If it doesn't exist, then line is set to 0. Line is what is being added to the income.
        return 0

    try:
        # I read the lines into a variable "fileLines"
        fileLines = myFile.readlines()
        # I get the first line of the file, which should store the income number.
        line = fileLines[0]
    except:
        # If the file doesn't exist, line is just 0.
        return 0
    
    # Income gained is set to 0 -- just to initialize it as an integer.
    incomeGained = 0
    # Income gained is whatever line is. Line represents what exists in the file.
    incomeGained += float(line)
    # I return the float version of the income gained.
    return incomeGained


# Returns a float value of expenses.
def getExpenses(userName):
    # Sets the filename to whatever the username is and .txt at the end.
    fileName = userName + ".txt"
    try:
        # It tried to open the file if it exists.
        myFile = open(fileName, "r")
    except:
        # If it doesn't exist, then it just returns 0.
        return 0
    try:
        # My program tries to read the lines off the file
        fileLines = myFile.readlines()
        line = fileLines[1]
    except:
        # If it can't read the file, it will just assume that a file doesn't exist,
        # and therefore returns a 0.
        return 0
    expenses = 0
    # Sets expenses to a float.
    expenses += float(line)
    return expenses


# Gets the float value of prices.
def getPrices(userName):
    # Sets the filename to whatever the user name is and adds a .txt at the end.
    fileName = userName + ".txt"
    try:
        # If the file can open, then we assume that there is a value in it.
        myFile = open(fileName, "r")
    except:
        # If it can't open, we simply return 0 since the file doesn't exist.
        return 0

    # The code below gets the current price of our expenses.
    try:
        # I try to read the 2nd line from the file, which represents the price.
        fileLines = myFile.readlines()
        line = fileLines[2]
    except:
        # If I can't reat it, then there is no price and I return 0.
        return 0
    totalCost = 0
    # I set the line to a float value.
    totalCost += float(line)
    return totalCost


# Checks to see if you can spend a specific amount of money.
def can_I_Spend_It(userName, howMuchIwantToSpend):
    return (getPrices(userName) - howMuchIwantToSpend)/12


# This function adds an item to the user file.
def addItem(userName, price, interval):
    # Sets the filename to the current user with a .txt appended to the user's name.
    fileName = userName + ".txt"

    try:
        # Checks to see if you can open the username.txt file.
        myFile = open(fileName, "r")
    except:
        # If not, then we make the username file.
        myFile = open(fileName, "x")

    # Gets the income float value.
    incomeGained = getIncome(userName)

    # Gets the expenses float value.
    expenses = getExpenses(userName)

    # Gets the prices float value.
    totalCost = getPrices(userName)

    # Sets the interval to uppercase for later comparison.
    interval = (interval.upper())
    # Sets the price string to a float.
    price = float(price)

    # I multiply the price to set it to yearly standards.
    if(interval == "MONTHLY"):
        price = price*12
    elif(interval == "WEEKLY"):
        price = price*52
    elif(interval == "DAILY"):
        price = price*365

    # I append price to the total cost of the current price.
    totalCost += price

    # If price is positive, I add it to income. If it's negative, I add it to expenses.
    if(price > 0):
        incomeGained += price
    else:
        expenses += price

    # I open the file to edit it.
    myFile = open(fileName, "w")
    # I set "incomeGained" to a string.
    incomeGained = str(incomeGained)
    # I set "expenses" to a string.
    expenses = str(expenses)
    # I set "totalCost" to a string.
    totalCost = str(totalCost)
    # I write all the values into the file.
    myFile.write(incomeGained + "\n")
    myFile.write(expenses + "\n")
    myFile.write(totalCost + "\n\n")


# I technically don't need this, but it's just for the frontend so people don't get confused
# when they don't find "addIncome."
def addIncome(userName, price, interval):
    addItem(userName, price, interval)


# I just invert the price value here -- since an expense is a loss of money.
def addExpense(userName, price, interval):
    price = float(price)
    price *= -1
    price = str(price)
    addItem(userName, price, interval)


# I print the .txt file. This is purely for testing purposes.
def printList(userName):
    # I create the filename to be whateer the username is with .txt appended on to it. 
    fileName = userName + ".txt"

    try:
        # If this file exists, it will be opened.
        myFile = open(fileName, "r")
    except:
        # If it doesn't, then it will be created.
        myFile = open(fileName, "x")

    # I open the file
    myFile = open(fileName, "r")
    # I print the contents of the file.
    print(myFile.read())


# This just prints out the help menu.
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
    print("Type \"PNUM\" or \"PRICESNUMBER\" to get the total expenses.")
    print("")   # This is just for an extra endline at the end of my menu.


# This deletes the contents of the user's .txt file.
def deleteAllData(userName):
    # I load the username and append .txt so I can access the .txt file.
    fileName = userName + ".txt"

    try:
        # I try to open the file to see if it exists.
        myFile = open(fileName, "r")
    except:
        # If it doesn't exist, then I create it.
        myFile = open(fileName, "x")

    # I open the file.
    myFile = open(fileName, "w")
    # I set the file to have nothing written in it.
    myFile.write("")
