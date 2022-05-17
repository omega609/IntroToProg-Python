# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Omar Lozano,05.12.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = 'ToDoList.txt' # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open('ToDoList.txt', "a")
dicRow = {"Task": "Write Script", "Priority": "High"}  # Make the first dictionary item for a list
objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
lstTable =[dicRow]  # Create list with the dictionary item
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable: # Iterating through items in list and printing out as a row
            print(row)

        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task: ")  # Have user enter a new task
        strPriority = input("Enter the priority: ")  # Have user enter new priority
        dicRow = {"Task": strTask, "Priority": strPriority.strip()} # Creating new dictionary item, to add to lstTable
        lstTable.append(dicRow)  # Append new dictionary item to list
        print(lstTable)  # Show user new item added

        continue

    # Step 5 - Remove an existing item from the list/Table
    elif (strChoice.strip() == '3'):
        strTaskRemove = input("Enter the task to remove: ")
        for row in lstTable:  # Iterate through list
            if row["Task"].lower() == strTaskRemove.lower():  # Looking for a key that matches item entered by user
                lstTable.remove(row)  # Remove both key and value from list
        print(strTaskRemove, "has been removed")  # Letting user know item removed

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")  # Appending any new dictionary items to list
        objFile.close()
        print("Your tasks have been saved to the file 'Todolist.txt' ")  # Let user know item has been added to file

        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("You have exited the program") # Let user know they have successfully exited program
        break  # and Exit the program
