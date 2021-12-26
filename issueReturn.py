# Importing ALl Functions From The utils file
from utils import *
# Importing datetime module
from datetime import date
# Importing PrettyTable from prettyprints module to print tables
from prettytable import PrettyTable
# Importing sqlData
import sqlData

# Setting The Fine per Day Variable
FINE_PER_DAY = 0.5 # 50 paise or 5 rupees

# Creating The Issue Book Function
def issueBook():
    # Try Catch Block
    try:
        # Taking User Inputs
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")

        # Executing SQL Query
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)

        # Creating Found Variable
        found = False
        for i in Cursor:
            # Storing Hashed User Password To Compare it
            HASHED_USER_PASSWORD = i[1]
            # Changing Found Variable TO True
            found = True

        # If Not Found Raising Exception
        if(not found):
            raise Exception(f"{Colors.FAIL}User Not Found{Colors.ENDC}")
        
        # Closing the Connection
        Cursor.close()
        cnx.close()

        # Getting User Input For Password
        USER_PASSWORD = input(f"{Colors.OKCYAN}Enter Password : {Colors.ENDC}")

        # If Passwords Do not Match Raising an Exception
        if(not checkPassword(USER_PASSWORD, HASHED_USER_PASSWORD)):
            raise Exception(f"{Colors.FAIL}Wrong Password{Colors.ENDC}")

        # Getting Input From User
        BOOK_ISBN,DATE_OF_ISSUE = input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"),date.today()
        
        # Executing SQL Query
        query = 'insert into issues Values(%s,%s,%s);'
        data = (BOOK_ISBN,USER_NAME,DATE_OF_ISSUE)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query,data)
        # Clearing Screen For Better Presentation
        clearScreen()
        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Issue Success")
    except Exception as err:
        clearScreen()
        print(err)

def displayIssuedBooks():
    # Try Catch Block
    try:
        # Executing SQL Query
        query = "select * from issues;"
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)

        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["Book ISBN","Username","Date of Issue"]

        for i in Cursor:
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[2],"%d-%m-%Y")
            x.add_row([i[0],i[1],dateString])

        # Printing The Table
        print(x)

        # Closing the Connection
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))

def returnIssuedBooks():
    # Try Catch Block
    try:
        # Taking User Input
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")

        # Executing SQL Query
        query = 'select * from issues where username = %s;'
        data = (USER_NAME,)
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        # Creating PrettyTableObject
        x = PrettyTable()
        # Adding Field Names
        x.field_names = ["Book ISBN","User Name","Date Of Issue"]

        # Creating Found Variable
        found = False
        for i in Cursor:
            # Storing Book Data
            BOOK_ISBN = i[0]
            DATE_ISSUED = i[2]
            # Using Datetime strftime to convert datetime object to string
            dateString = date.strftime(i[2],"%d-%m-%Y")
            data = [i[0],i[1],dateString]
            x.add_row(data)
            # Changing Found Variable TO True
            found = True

        # Printing Error If Not Found
        if(not found):
            x.add_row(["No","Issue Record","Found"])
            print(x)
            return

        # Printing The Table
        print(x)
        # Closing the Connection
        Cursor.close()
        cnx.close()

        # Creating Days Issued Variable
        DAYS_ISSUED = 0
        # Calculating Days Issued
        try:
            DAYS_ISSUED = int(str(date.today() - DATE_ISSUED).split()[0]) - 7
        except:
            DATE_ISSUED = 0

        # Changing Days To 0 if it is negative
        if DAYS_ISSUED < 0:
            DAYS_ISSUED = 0

        # Getting User Input For Confirmation
        choice = input(f"{Colors.WARNING} Do You Wish To Return The Book with ISBN {BOOK_ISBN} Associated With User {USER_NAME} The Fine Applicable Would Be Rs. {DAYS_ISSUED * FINE_PER_DAY}(y/n): ")

        # Returning if choice is not y/Y
        if(choice.lower()!="y"):
            clearScreen()
            return
        
        # Executing SQL Query
        query = 'delete from issues where username=%s'
        data = (USER_NAME,)
        # Executing The Query From Function in utils file
        res = executeSQLCommitQuery(query,data)
        # Clearing Screen For Better Presentation
        clearScreen()
        # If the result comes as a string it means a error has been raised else Member Get Added
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Issued Record Deleted")
    except Exception as err:
        clearScreen()
        print(err)

def menu():
    # Creating The Issue/Return Options Dictionary
    issueReturnBookMenuOptions = {
        1:["Issue Book",issueBook],
        2:["Display Issued Books",displayIssuedBooks],
        3:["Return Issued Books",returnIssuedBooks],
        4:["Return To Main Menu"]
    }
    # Running The Show Menu Function From Utils File On The Main Menu Options Dictionary
    showMenu("Issue Return Menu",issueReturnBookMenuOptions,menuSpacing) # Passing Members Menu as Menu Title and Menu Spacing from utils file to center the menu heading