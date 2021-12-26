# Importing ALl Functions From The utils file
from utils import *
# Importing datetime module
from datetime import date
# Importing PrettyTable from prettyprints module to print tables
from prettytable import PrettyTable
# Importing sqlData
import sqlData

# Creating The Add Member Function


def addMember():
    # Try Catch Block
    try:
        # Taking User Inputs
        USER_NAME, USER_PASSWORD, DATE_OF_REGISTRATION = input(
            f"{Colors.OKCYAN}Enter User Name : "), input(f"Enter User Password : {Colors.ENDC}"), date.today()

        # Checking If length of USER_NAME is less tand 4 or USER_PASSWORD is less than 4
        # If raising an Exception
        if(len(USER_NAME) < 4 or len(USER_PASSWORD) < 4):
            raise Exception(f"{Colors.FAIL}Invalid Input{Colors.ENDC}")

        # Hashing User Password To Save it in sql table
        USER_PASSWORD = hashPassword(USER_PASSWORD)

        # Executing SQL Query
        query = "INSERT INTO members VALUES (%s, %s, %s);"
        data = (USER_NAME, USER_PASSWORD, DATE_OF_REGISTRATION)

        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen For Better Presentation
        clearScreen()
        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Added")
    except:
        clearScreen()
        print("Invalid Input")

# Creating Display members Function


def displayMembers():
    # Try-Catch Block
    try:
        # Wrting SQL Query and Executing it
        # The Function cannot be used here because Cursor object gets deleted from memory as the function ends
        query = "select * from members;"
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["User Name", "Date Of Registation"]

        # Navigating In Cursor Object To Add Values TO PrettyTable Object
        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[2], "%d-%m-%Y")
            x.add_row([i[0], dateString])

        # Printing The Table
        print(x)
        # Closing the Connection
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))


def searchMember():
    # try Catch Block
    try:
        # getting the user input
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")

        # Executng The Query
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query, data)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["User Name", "Date of Registation"]

        # Creating Found Variable
        found = False
        # Navigating In Cursor Object To Add Values TO PrettyTable Object
        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[2], "%d-%m-%Y")
            data = [i[0], dateString]
            x.add_row(data)
            # Changing Found Variable TO True
            found = True

        # If Not Found Print Not Found
        if(not found):
            x.add_row(["No User", "Record Found"])

        # Printing The Table
        print(x)
        # Closing the Connection
        Cursor.close()
        cnx.close()

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)


def deleteMember():
    # try-Catch Blck
    try:
        # getting the user input
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")

        # Executng The Query
        query = 'delete from Members where username=%s;'
        data = (USER_NAME,)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen
        clearScreen()

        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Deleted")
    except:
        clearScreen()
        print("Invalid Input")


def updateMemberPassword():
    # Try Catch Block
    try:
        # Taking User Input
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")

        # Executing SQL Query
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query, data)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["User Name", "Date Of Registation"]

        # Creating Found Variable
        found = False
        for i in Cursor:
            # Storing Old Hashed Password to Compare
            USER_PASSWORD = i[1]
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[2], "%d-%m-%Y")
            data = [i[0], dateString]
            x.add_row(data)
            # Changing Found Variable TO True
            found = True

        # Printing Error If Not Found
        if(not found):
            x.add_row(["No User", "Record Found"])
            print(x)
            return

        # Printing The Table
        print(x)
        # Closing the Connection
        Cursor.close()
        cnx.close()

        # Getting User Input For Old Password
        OLD_USER_PASSWORD = input(
            f"{Colors.OKCYAN}Enter Your Old Password : {Colors.ENDC}")

        # If Passwords Do not Match Raising an Exception
        if(not checkPassword(OLD_USER_PASSWORD, USER_PASSWORD)):
            clearScreen()
            raise Exception(f"{Colors.FAIL}Wrong Password{Colors.ENDC}")

        # Getting New Password Input From User
        USER_PASSWORD = input(
            f"{Colors.OKCYAN}Enter New User Password : {Colors.ENDC}")

        # Checking If length of USER_PASSWORD is less than 4
        # If raising an Exception
        if(len(USER_PASSWORD) < 4):
            raise Exception(f"{Colors.FAIL}Invalid Input{Colors.ENDC}")

        # Hashing New User Password To Save it in sql table
        USER_PASSWORD = hashPassword(USER_PASSWORD)

        # Executing SQL Query
        query = 'UPDATE members set password=%s where username=%s'
        data = (USER_PASSWORD, USER_NAME)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen For Better Presentation
        clearScreen()
        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Password Updated")

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)


def menu():
    # Creating The Menu Options Dictionary
    membersMenuOptions = {
        1: ["Add Member", addMember],
        2: ["Display Members", displayMembers],
        3: ["Search Members", searchMember],
        4: ["Delete Member", deleteMember],
        5: ["Update Member Password", updateMemberPassword],
        6: ["Return To Main Menu"]
    }
    # Running The Show Menu Function From Utils File On The Main Menu Options Dictionary
    # Passing Members Menu as Menu Title and Menu Spacing from utils file to center the menu heading
    showMenu("Members Menu", membersMenuOptions, menuSpacing)
