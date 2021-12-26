# This is A One Time Run File After Running It You May Delete It
# This set ups the environment required to run the python program successfully
# Just Make Sure You Do Not Have Any Database name library in your pc beforerunning this file

# Sql Connector
import mysql.connector
# SQL Data File
import sqlData

# Establishing The Connection
mydb = mysql.connector.connect(
    host="localhost",
    user=sqlData.SQL_USERNAME,
    password=sqlData.SQL_PASSWORD
)

# Creating The Cursor Object
mycursor = mydb.cursor()
# Executing Commands
# Creating Database Library
mycursor.execute("CREATE DATABASE Library")
# Swithing To Database Library
mycursor.execute("use Library")

# Creating Tables :
# Books
mycursor.execute(
    "CREATE Table books(Book_Name varchar(20),ISBN varchar(15),Author varchar(20),Date_Of_Publishing DATE,PRIMARY KEY (ISBN))")
# Members
mycursor.execute(
    "CREATE Table members(username varchar(20),password varchar(100),Date_Of_Registration DATE,PRIMARY KEY (username))")
# Issues
mycursor.execute("CREATE Table issues(book_isbn varchar(15),username varchar(20),Date_Of_Issue DATE,PRIMARY KEY (username),FOREIGN KEY (username) REFERENCES members(username),FOREIGN KEY (book_isbn) REFERENCES books(ISBN))")
