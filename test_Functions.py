import os
import time
from Backend_Functions import deleteAllData
from Backend_Functions import addItem
from Backend_Functions import getExpenses
from Backend_Functions import addExpense

# I test the "deleteAllData" function to see if it creates a file.
def test_FileCreation_deleteAllData():
# The three lines below are just the standard procedure for making a file.
    userName = "deleteMe1"
    deleteAllData(userName)
    fileName = userName + ".txt"

    try:
        # I try to see if I can open the file.
        myFile = open(fileName, "r")
        # If the file opens, that means it exists and the test passes.
        assert True
    except:
        # If the files doesn't, it'll return an error and the exception will catch it here.
        assert False

# This test checks to see if "addItem" creates a file when called.
def test_FileCreation_addItem():
# The three lines below are just the standard procedure for making a file.
    userName = "deleteMe2"
    addItem(userName, "1.00", "MONTHLY")
    fileName = userName + ".txt"

    try:
        # I try to see if I can open the file.
        myFile = open(fileName, "r")
        # If the file opens, that means it exists and the test passes.
        assert True
    except:
        # If the files doesn't, it'll return an error and the exception will catch it here.
        assert False

# The file below checks and tests to see if the "deleteAllData" really does delete all the data
# in a file.
def test_deleteAllData():
# The three lines below are just the standard procedure for making a file.
    userName = "deleteMe3"
    deleteAllData(userName)
    fileName = userName + ".txt"

    try:
        myFile = open(fileName, "r")
        # If the file contains nothing, then the function works.
        if(myFile.read() == ""):
            assert True
        else:
        # Otherwise, the function failed.
            assert False
    except:
        # This is just to catch if an unexpected error had occurred.
        assert False

# This test function checks to see if a price was made and added to the file.
def test_data_inputting():
# The three lines below are just the standard procedure for making a file.
    userName = "deleteMe4"
    fileName = userName + ".txt"

    try:
        # This adds the item to file "deleteMe4.txt."
        addItem(userName, "1.00", "YEARLY")
        myFile = open(fileName, "r")
        getLines = myFile.readlines()
        # This checks to see if the lines match up with what they're supposed to display.
        if(getLines[0] == "1.0\n" and getLines[1] == "0\n" and getLines[2] == "1.0\n"):
            assert True
        else:
            # If they don't match up, then the test fails.
            print(getLines[0])
            assert False
    except:
        # This is just to catch if an unexpected error had occurred.
        assert False

# This function tests if the "getExpenses()" function works correctly.
def test_expense_retrieval():
    # The line below is just the standard procedure for making a file.
    userName = "deleteMe5"
    
    try:
        # I try to add an expense to a file.
        addExpense(userName, "1.00", "DAILY")
        # If the expense is -365 -- which it's supposed to be, I assert True.
        if(getExpenses(userName) == -365.0):
            assert True
        else:
            # If it's not -365, I assert false.
            assert False
    except:
        # If the file doesn't run, I also assert false.
        assert False

# this "test" just deletes all the files created from the previous tests.
def test_deletion():
    # I force the program to wait 5 seconds before deleting everything, so I can check if the files were
    # actually made to begin with.
    time.sleep(5)
    os.remove("deleteMe1.txt")
    os.remove("deleteMe2.txt")
    os.remove("deleteMe3.txt")
    os.remove("deleteMe4.txt")
    os.remove("deleteMe5.txt")
