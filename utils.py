# **********************************Imports****************************************
# OS Module To Implement The Clear Screen Function
import os
# MySQL Connector
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
# bcrypt library to hash passwords
import bcrypt
# Local Python File sqlData containing the sql Username ,Password and Database Name
import sqlData


# **********************************General Functions****************************************
# Class Colors to print clorful text in python terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


#  MenuSpacing Variable To Center The menu Heading by adding spaces as prefix
menuSpacing = "          "

# Function To Print Divider in Green Color


def divider():
    print(f"{Colors.OKGREEN}=============================={Colors.ENDC}")

# Function To Print Invalid Input in Red Color


def invalidInput():
    print(f"{Colors.FAIL}Invalid Input Enter A Choice From the Menu Above{Colors.ENDC}")
    divider()


def clearScreen():
    os.system("cls")


# **********************************Menu Functions****************************************
# Function To Print Menu
def showMenu(menuTitle, menuOptions, menuSpacing):
    while True:
        print(f"{Colors.HEADER}{menuSpacing}{menuTitle} {Colors.ENDC}")
        divider()
        for choice, statement in menuOptions.items():
            print(
                f"{Colors.OKBLUE}{Colors.BOLD}{choice} - {statement[0]}{Colors.ENDC}")
        try:
            choice = int(input("Enter Choice : "))
            clearScreen()
            if(choice >= 1 and choice <= len(menuOptions.keys())):
                if(choice == len(menuOptions.keys())):
                    break
                try:
                    menuOptions[choice][1]()
                except Exception as e:
                    print(e)
                divider()
            else:
                invalidInput()
        except:
            clearScreen()
            invalidInput()


# **********************************SQL Functions Start****************************************
# SQL Function To Add/Delete and Update Data in the database
# NOTE : Cannot Be Used To Read Data From Cursor Object as Connection is Broken as Soon As The Function Ends
def executeSQLCommitQuery(query, data):
    try:
        cnx = connection.MySQLConnection(
            user=sqlData.SQL_USERNAME, password=sqlData.SQL_PASSWORD, host='localhost', database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query, data)
        cnx.commit()
        Cursor.close()
        cnx.close
        return Cursor
    except mysql.connector.Error as err:
        return handleSQLException(err)

# SQL Function To Handle All Major SQL ErrorCodes else return error message


def handleSQLException(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return ("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return ("Database does not exist")
    elif err.errno == 1062:
        return ("Duplicate Entry")
    elif err.errno == 1451:
        return ("Cannot Delete A Entry that Is A Member Of Another Table, the book or user must be issued to someone try removing the issued record first")
    else:
        return (err)


# **********************************Password Functions****************************************
# Hash Password String After Adding Salt using bcrypt
def hashPassword(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

# Compare Password Strings wsing bcrypt


def checkPassword(password, hashedPassword):
    return bcrypt.checkpw(password.encode("utf-8"), hashedPassword.encode("utf-8"))
