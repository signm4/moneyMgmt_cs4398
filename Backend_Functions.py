import numpy as np

def addItem(myList):
    itemName = input("Enter item name: ")
    price = input("Enter item price: ")
    myList.append([itemName, price])

def printList(list):
    for i, item in enumerate(list):
        print(i + 1, item)

def basePrice(item):
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

# Add a changeItem function.

# Add a data .itt file or something similar to read data from and into files to save into 
# the program.

# Add a percent function that prints the percentages of all expenses.

# Document everything







print("Start Program")

EXIT = False
priceList = [["Food", 10.23, "daily"],["Gas", 15.11, "weekly"],["Rent", 33.00, "monthly"],["Water", 2.99, "daily"],["Clothes", 20.54, "monthly"]]
print("Enter \"h\" to ask for help.")

while EXIT is not True:
    userChoice = input("Input: ")
    userChoice = userChoice.upper()
    if userChoice == 'H' or userChoice == 'HELP':
        printHelpMenu()
    elif userChoice == 'E' or userChoice == 'EXIT':
        EXIT = True
    elif userChoice == 'P' or userChoice == 'PRINT' or userChoice == 'PRINTLIST':
        printList(priceList)
    elif userChoice == 'N' or userChoice == 'NEW' or userChoice == 'NEWITEM':
        addItem(priceList)
    elif userChoice == 'PA' or userChoice == 'PRINTAVERAGE':
        printAverage(priceList)
    elif userChoice == 'D' or userChoice == "DELETE" or userChoice == "DELETEITEM":
        priceList = deleteItem(priceList)
    else:
        print("ERROR: COMMAND NOT RECOGNIZED")

print("Program Exit")
