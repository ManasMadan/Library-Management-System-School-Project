import os
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import sqlData
import bcrypt

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

menuSpacing = "          "

def divider():
    print(f"{Colors.OKGREEN}=============================={Colors.ENDC}")

def invalidInput():
    print(f"{Colors.FAIL}Invalid Input Enter A Choice From the Menu Above{Colors.ENDC}")
    divider()

def showMenu(menuTitle,menuOptions,menuSpacing):
    while True:
        print(f"{Colors.HEADER}{menuSpacing}{menuTitle} {Colors.ENDC}")
        divider()
        for choice,statement in menuOptions.items():
            print(f"{Colors.OKBLUE}{Colors.BOLD}{choice} - {statement[0]}{Colors.ENDC}")
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

def clearScreen():
    os.system("cls")

def executeSQLCommitQuery(query,data):
    try:
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        return Cursor
    except mysql.connector.Error as err:
        return handleSQLException(err)

def handleSQLException(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return ("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return ("Database does not exist")
    elif err.errno == 1062:
        return ("Duplicate Entry")
    else:
        return (err)

def hashPassword(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def checkPassword(password, hashedPassword):
    return bcrypt.checkpw(password.encode("utf-8"), hashedPassword.encode("utf-8"))