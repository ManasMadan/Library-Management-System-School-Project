from utils import *
from datetime import date
import sqlData
from prettytable import PrettyTable

def addBook():
    try:
        BOOK_NAME,BOOK_ISBN,BOOK_AUTHOR,BOOK_PUBLISHING_DATE,BOOK_PUBLISHING_MONTH,BOOK_PUBLISHING_YEAR = input(f"{Colors.OKCYAN}Enter Book Name : "),int(input("Enter Book ISBN : ")),input("Enter Book Author : "),int(input("Enter Book Publishing Date : ")),int(input("Enter Book Publishing Month : ")),int(input(f"Enter Book Publishing Year : {Colors.ENDC}"))
        query = "INSERT INTO books VALUES (%s, %s, %s, %s);"
        data = (BOOK_NAME,BOOK_ISBN,BOOK_AUTHOR,date(BOOK_PUBLISHING_YEAR,BOOK_PUBLISHING_MONTH,BOOK_PUBLISHING_DATE))
        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Book Added")
    except:
        clearScreen()
        print("Invalid Input")

def displayBooks():
    try:
        query = "select * from books;"
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)
        x = PrettyTable()
        x.field_names = ["Book Name","Book ISBN","Book Author","Date Of Publishing"]
        for i in Cursor:
            dateString = date.strftime(i[3],"%d-%m-%Y")
            x.add_row([i[0],i[1],i[2],dateString])
        print(x)
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))

def searchBook():
    try:
        BOOK_ISBN = int(input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))
        query = 'select * from books where ISBN = "%s";'
        data = (BOOK_ISBN,)

        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        x = PrettyTable()
        x.field_names = ["Book Name","Book ISBN","Book Author","Date Of Publishing"]

        found = False
        for i in Cursor:
            dateString = date.strftime(i[3],"%d-%m-%Y")
            data = [i[0],i[1],i[2],dateString]
            x.add_row(data)
            found = True
        
        if(not found):
            x.add_row(["No","Book","Record","Found"])

        print(x)
        Cursor.close()
        cnx.close()

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)

def deleteBook():
    try:
        BOOK_ISBN= int(input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))
        query = 'DELETE FROM books where ISBN="%s"'
        data = (BOOK_ISBN,)
        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Book Deleted")
    except:
        clearScreen()
        print("Invalid Input")
   
def updateBook():
    try:
        BOOK_ISBN = int(input(f"{Colors.OKCYAN}Enter Book ISBN : {Colors.ENDC}"))
        query = 'select * from books where ISBN = "%s";'
        data = (BOOK_ISBN,)

        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        x = PrettyTable()
        x.field_names = ["Book Name","Book ISBN","Book Author","Date Of Publishing"]

        found = False
        for i in Cursor:
            dateString = date.strftime(i[3],"%d-%m-%Y")
            data = [i[0],i[1],i[2],dateString]
            x.add_row(data)
            found = True

        if(not found):
            x.add_row(["No","Book","Record","Found"])
            print(x)
            return

        print(x)

        Cursor.close()
        cnx.close()

        BOOK_NAME,BOOK_AUTHOR,BOOK_PUBLISHING_DATE,BOOK_PUBLISHING_MONTH,BOOK_PUBLISHING_YEAR = input(f"{Colors.OKCYAN}Enter Book Name : "),input("Enter Book Author : "),int(input("Enter Book Publishing Date : ")),int(input("Enter Book Publishing Month : ")),int(input(f"Enter Book Publishing Year : {Colors.ENDC}"))
        query = 'UPDATE books set Book_Name=%s,Author=%s,Date_Of_Publishing=%s where ISBN="%s"'
        data = (BOOK_NAME,BOOK_AUTHOR,date(BOOK_PUBLISHING_YEAR,BOOK_PUBLISHING_MONTH,BOOK_PUBLISHING_DATE),BOOK_ISBN)
        res = executeSQLCommitQuery(query,data)
        clearScreen()
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
    booksMenuOptions = {1:["Add Book",addBook],2:["Display Books",displayBooks],3:["Delete Book",deleteBook],4:["Search Book",searchBook],5:["Update Book",updateBook],6:["Return To Main Menu"]}
    showMenu("Books Menu",booksMenuOptions,menuSpacing)