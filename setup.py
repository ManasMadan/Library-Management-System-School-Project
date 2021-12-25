import mysql.connector
import sqlData

mydb = mysql.connector.connect(
  host="localhost",
  user=sqlData.SQL_USERNAME,
  password=sqlData.SQL_PASSWORD
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Library")
mycursor.execute("use Library")
mycursor.execute("CREATE Table books(Book_Name varchar(20),ISBN varchar(15),Author varchar(20),Date_Of_Publishing DATE,PRIMARY KEY (ISBN))")
mycursor.execute("CREATE Table members(username varchar(20),password varchar(100),Date_Of_Registration DATE,PRIMARY KEY (username))")
mycursor.execute("CREATE Table issues(book_isbn varchar(15),username varchar(20),Date_Of_Issue DATE,PRIMARY KEY (username),FOREIGN KEY (username) REFERENCES members(username),FOREIGN KEY (book_isbn) REFERENCES books(ISBN))")