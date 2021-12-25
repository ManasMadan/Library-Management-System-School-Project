from utils import *
from datetime import date
import sqlData
from prettytable import PrettyTable

FINE_PER_DAY = 0.5

def issueBook():
    try:
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)

        found = False
        for i in Cursor:
            HASHED_USER_PASSWORD = i[1]
            found = True

        if(not found):
            raise Exception(f"{Colors.FAIL}User Not Found{Colors.ENDC}")
        
        Cursor.close()
        cnx.close()

        USER_PASSWORD = input(f"{Colors.OKCYAN}Enter Password : {Colors.ENDC}")

        if(not checkPassword(USER_PASSWORD, HASHED_USER_PASSWORD)):
            raise Exception(f"{Colors.FAIL}Wrong Password{Colors.ENDC}")

        BOOK_ISBN,DATE_OF_ISSUE = input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"),date.today()
        
        query = 'insert into issues Values(%s,%s,%s);'
        data = (BOOK_ISBN,USER_NAME,DATE_OF_ISSUE)
        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Issue Success")
    except Exception as err:
        clearScreen()
        print(err)

def displayIssuedBooks():
    try:
        query = "select * from issues;"
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)
        x = PrettyTable()
        x.field_names = ["Book ISBN","Username","Date of Issue"]
        for i in Cursor:
            dateString = date.strftime(i[2],"%d-%m-%Y")
            x.add_row([i[0],i[1],dateString])
        print(x)
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))

def returnIssuedBooks():
    try:
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")
        query = 'select * from issues where username = %s;'
        data = (USER_NAME,)

        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        x = PrettyTable()
        x.field_names = ["Book ISBN","User Name","Date Of Issue"]

        found = False
        for i in Cursor:
            BOOK_ISBN = i[0]
            DATE_ISSUED = i[2]
            dateString = date.strftime(i[2],"%d-%m-%Y")
            data = [i[0],i[1],dateString]
            x.add_row(data)
            found = True

        if(not found):
            x.add_row(["No","Issue Record","Found"])
            print(x)
            return

        print(x)
        Cursor.close()
        cnx.close()

        DAYS_ISSUED = 0
        try:
            DAYS_ISSUED = int(str(date.today() - DATE_ISSUED).split()[0]) - 7
        except:
            DATE_ISSUED = 0

        if DAYS_ISSUED < 0:
            DAYS_ISSUED = 0

        choice = input(f"{Colors.WARNING} Do You Wish To Return The Book with ISBN {BOOK_ISBN} Associated With User {USER_NAME} The Fine Applicable Would Be Rs. {DAYS_ISSUED * FINE_PER_DAY}(y/n): ")

        if(choice.lower()=="n"):
            clearScreen()
            return
        
        query = 'delete from issues where username=%s'
        data = (USER_NAME,)

        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Issued Record Deleted")
    except Exception as err:
        # clearScreen()
        print(err)

def menu():
    issueReturnBookMenuOptions = {1:["Issue Book",issueBook],2:["Display Issued Books",displayIssuedBooks],3:["Return Issued Books",returnIssuedBooks],4:["Return To Main Menu"]}
    showMenu("Issue Return Menu",issueReturnBookMenuOptions,menuSpacing)