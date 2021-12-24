from utils import *

def addBook():
    print("Add Book")
def displayBooks():
    print("Display Books")
def removeBook():
    print("Remove Book")
def searchBook():
    print("Search Book")
def deleteBook():
    print("Delete Book")
def updateBook():
    print("Update Book")

def menu():
    booksMenuOptions = {1:["Add Book",addBook],2:["Display Books",displayBooks],3:["Remove Book",removeBook],4:["Search Book",searchBook],5:["Delete Book",deleteBook],6:["Update Book",updateBook],7:["Return To Main Menu"]}
    showMenu("Books Menu",booksMenuOptions,menuSpacing)