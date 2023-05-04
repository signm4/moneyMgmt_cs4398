from Backend_Functions import printList
from Backend_Functions import addItem
from Backend_Functions import printHelpMenu
from Backend_Functions import deleteAllData
from Backend_Functions import addIncome
from Backend_Functions import addExpense
from Backend_Functions import getIncome
from Backend_Functions import getExpenses
from Backend_Functions import getPrices

print("Start Program")

EXIT = False

# This checks to see if the string passed through the argument is either "DAILY", "WEEKLY",
# "MONTHLY", or "YEARLY".
def checkIfValidInterval(intervalString):
    if(intervalString == "DAILY" or intervalString == "WEEKLY" or intervalString == "MONTHLY" or intervalString == "YEARLY"):
        return True
    else:
        return False

# This prompts the user to type in a specified interval such as "DAILY", "WEEKLY",
# "MONTHLY", or "YEARLY".
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

# This asks for a valid number -- so it isn't a letter and only a number.
def askForNumber():
        # The program takes a string input from the user.
        priceChoice = input("Choose a price for the item: ")
        notValidChoice = True
        while(notValidChoice):
            try:
                # If the string input can be turned into a integer or float, then it's a
                # Valid value. Otherwise, it's invalid since it's most likely a character.
                priceChoice = float(priceChoice)
                notValidChoice = False
            except:
                priceChoice = input("ERROR: Please type an integer or a float: ")
        # Turns the integer / float back into a string, since it needs to return into the program.
        return str(priceChoice)

# Here's the main code.
userName = "null"
# The program prompts the user for a userName.
userName = input("Select Username: ")

while EXIT is not True:
    # This while-loop asks for the user's input every loop.
    userChoice = input("Input: ")
    # This capitalizes all of the letters in the user's string.
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
        deleteAllData(userName)
    elif userChoice == 'INC' or userChoice == 'INCOME':
        priceChoice = askForNumber()
        intervalChoice = askForInterval()
        addIncome(userName, priceChoice, intervalChoice)
    elif userChoice == 'EXP' or userChoice == 'EXPENSE':
        priceChoice = askForNumber()
        intervalChoice = askForInterval()
        addExpense(userName, priceChoice, intervalChoice)
    elif userChoice == 'INCNUM' or userChoice == 'INCOMENUMBER':
        print(getIncome(userName))
    elif userChoice == 'EXPNUM' or userChoice == 'EXPENSESNUMBER':
        print(getExpenses(userName))
    elif userChoice == 'PNUM' or userChoice == 'PRICESNUMBER':
        print(getPrices(userName))
    else:
        print("ERROR: COMMAND NOT RECOGNIZED")

print("Program Exit")
