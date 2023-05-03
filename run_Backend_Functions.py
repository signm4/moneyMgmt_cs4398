from Backend_Functions import printList
from Backend_Functions import addItem1
from Backend_Functions import addItem2
from Backend_Functions import pop
from Backend_Functions import printAverage
from Backend_Functions import deleteItem
from Backend_Functions import printHelpMenu

print("Start Program")

EXIT = False
priceList = [["Food", 10.23, "daily"],["Gas", 15.11, "weekly"],["Rent", 33.00, "monthly"],["Water", 2.99, "daily"],["Clothes", 20.54, "monthly"]]

'''
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
'''

print()
# addItem2("Protein Shakes", "5.00", "Daily")
# addItem2("Protein Shakes", "5.00", "Daily")
# addItem2("Protein Shakes", "5.00", "Daily")

# addItem1("5.00", "Daily")
# addItem1("5.00", "Daily")
# addItem1("5.00", "Daily")

pop()
printList()

print("Program Exit")
