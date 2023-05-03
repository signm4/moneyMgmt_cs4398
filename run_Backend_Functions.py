from Backend_Functions import printList
from Backend_Functions import addItem
from Backend_Functions import pop
from Backend_Functions import printHelpMenu
from Backend_Functions import addUser
from Backend_Functions import deleteAllData
from Backend_Functions import getAverage

print("Start Program")

EXIT = False
priceList = [["Food", 10.23, "daily"],["Gas", 15.11, "weekly"],["Rent", 33.00, "monthly"],["Water", 2.99, "daily"],["Clothes", 20.54, "monthly"]]

def checkIfValidInterval(intervalString):
    if(intervalString == "DAILY" or intervalString == "WEEKLY" or intervalString == "MONTHLY" or intervalString == "YEARLY"):
        return True
    else:
        return False

def askForInterval():
    intervalChoice = input("Choose an interval for the item: ")
    while(checkIfValidInterval(intervalChoice) == False):
        intervalChoice = intervalChoice.upper()
        if(intervalChoice == "D"):
            intervalChoice = "DAILY"
        elif(intervalChoice == "W"):
            intervalChoice = "WEEKLY"
        elif(intervalChoice == "M"):
            intervalChoice = "MONTHLY"
        elif(intervalChoice == "Y"):
            intervalChoice = "YEARLY"
        elif(checkIfValidInterval(intervalChoice) == False):
            intervalChoice = input("ERROR: PLEASE USE ONE OF THE OPTIONS: DAILY, WEEKLY, MONTHLY, YEARLY: ")
    return intervalChoice

def askForNumber():
        priceChoice = input("Choose a price for the item: ")
        notValidChoice = True
        while(notValidChoice):
            try:
                priceChoice = float(priceChoice)
                notValidChoice = False
            except:
                priceChoice = input("ERROR: Please type an integer or a float: ")
        return str(priceChoice)

userName = "null"
userName = input("Select Username: ")

while EXIT is not True:
    userChoice = input("Input: ")
    userChoice = userChoice.upper()
    if userChoice == 'H' or userChoice == 'HELP':
        printHelpMenu()
    elif userChoice == 'Q' or userChoice == 'QUIT':
        EXIT = True
    elif userChoice == 'P' or userChoice == 'PRINT':
        print()
        printList(userName)
    elif userChoice == 'N' or userChoice == 'NEW':
        priceChoice = askForNumber()
        intervalChoice = askForInterval()
        addItem(userName, priceChoice, intervalChoice)
    elif userChoice == 'D' or userChoice == "DELETE":
        pop(userName)
    elif userChoice == 'U' or userChoice == "USER":
        nameChoice = input("Choose a username: ")
        addUser(nameChoice)
    elif userChoice == 'DA' or userChoice == "DELETEALL":
        deleteAllData(userName)
    elif userChoice == 'TEST':
        getAverage(userName)
    else:
        print("ERROR: COMMAND NOT RECOGNIZED")

print("Program Exit")
