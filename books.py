# Importing ALl Functions From The utils file
from utils import *
# Importing datetime module
from datetime import date
# Importing PrettyTable from prettyprints module to print tables
from prettytable import PrettyTable
# Importing sqlData
import sqlData


def addBook():
    # Try Catch Block
    try:
        # Taking User Inputs
        BOOK_NAME, BOOK_ISBN, BOOK_AUTHOR, BOOK_PUBLISHING_DATE, BOOK_PUBLISHING_MONTH, BOOK_PUBLISHING_YEAR = input(f"{Colors.OKCYAN}Enter Book Name : "), int(input("Enter Book ISBN : ")), input(
            "Enter Book Author : "), int(input("Enter Book Publishing Date : ")), int(input("Enter Book Publishing Month : ")), int(input(f"Enter Book Publishing Year : {Colors.ENDC}"))

        # Executing SQL Query
        query = "INSERT INTO books VALUES (%s, %s, %s, %s);"
        data = (BOOK_NAME, BOOK_ISBN, BOOK_AUTHOR, date(
            BOOK_PUBLISHING_YEAR, BOOK_PUBLISHING_MONTH, BOOK_PUBLISHING_DATE))
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen For Better Presentation
        clearScreen()
        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Book Added")
    except:
        clearScreen()
        print("Invalid Input")


def displayBooks():
    # Try Catch Block
    try:
        # Executing SQL Query
        query = "select * from books;"
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["Book Name", "Book ISBN",
                         "Book Author", "Date Of Publishing"]
        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[3], "%d-%m-%Y")
            x.add_row([i[0], i[1], i[2], dateString])

        # Printing The Table
        print(x)

        # Closing the Connection
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))


def searchBook():
    # Try Catch Block
    try:
        # Taking User Input
        BOOK_ISBN = int(
            input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))

        # Executing SQL Query
        query = 'select * from books where ISBN = "%s";'
        data = (BOOK_ISBN,)
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query, data)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["Book Name", "Book ISBN",
                         "Book Author", "Date Of Publishing"]

        # Creating Found Variable
        found = False
        # Navigating In Cursor Object To Add Values TO PrettyTable Object
        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[3], "%d-%m-%Y")
            data = [i[0], i[1], i[2], dateString]
            x.add_row(data)
            # Changing Found Variable TO True
            found = True

        # If Not Found Print Not Found
        if(not found):
            x.add_row(["No", "Book", "Record", "Found"])

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


def deleteBook():
    # try-Catch Blck
    try:
        # getting the user input
        BOOK_ISBN = int(
            input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))

        # Executng The Query
        query = 'DELETE FROM books where ISBN="%s"'
        data = (BOOK_ISBN,)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen
        clearScreen()

        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Book Deleted")
    except:
        clearScreen()
        print("Invalid Input")


def updateBook():
    # Try Catch Block
    try:
        # Taking User Input
        BOOK_ISBN = int(
            input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))

        # Executing SQL Query
        query = 'select * from books where ISBN = "%s";'
        data = (BOOK_ISBN,)
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query, data)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["Book Name", "Book ISBN",
                         "Book Author", "Date Of Publishing"]

        # Creating Found Variable
        found = False
        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[3], "%d-%m-%Y")
            data = [i[0], i[1], i[2], dateString]
            x.add_row(data)
            # Changing Found Variable TO True
            found = True

        # Printing Error If Not Found
        if(not found):
            x.add_row(["No", "Book", "Record", "Found"])
            print(x)
            return

        # Printing The Table
        print(x)
        # Closing the Connection
        Cursor.close()
        cnx.close()

        # Getting User Input For New Details
        BOOK_NAME, BOOK_AUTHOR, BOOK_PUBLISHING_DATE, BOOK_PUBLISHING_MONTH, BOOK_PUBLISHING_YEAR = input(f"{Colors.OKCYAN}Enter Book Name : "), input("Enter Book Author : "), int(
            input("Enter Book Publishing Date : ")), int(input("Enter Book Publishing Month : ")), int(input(f"Enter Book Publishing Year : {Colors.ENDC}"))

        # Executing SQL Query
        query = 'UPDATE books set Book_Name=%s,Author=%s,Date_Of_Publishing=%s where ISBN="%s"'
        data = (BOOK_NAME, BOOK_AUTHOR, date(BOOK_PUBLISHING_YEAR,
                BOOK_PUBLISHING_MONTH, BOOK_PUBLISHING_DATE), BOOK_ISBN)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query, data)
        # Clearing Screen For Better Presentation
        clearScreen()

        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Book Record Updated")

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)


def menu():
    # Creating The Menu Options Dictionary
    booksMenuOptions = {
        1: ["Add Book", addBook],
        2: ["Display Books", displayBooks],
        3: ["Delete Book", deleteBook],
        4: ["Search Book", searchBook],
        5: ["Update Book", updateBook],
        6: ["Return To Main Menu"]
    }
    # Running The Show Menu Function From Utils File On The Main Menu Options Dictionary
    # Passing Members Menu as Menu Title and Menu Spacing from utils file to center the menu heading
    showMenu("Books Menu", booksMenuOptions, menuSpacing)
