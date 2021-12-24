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

booksMenuOptions = {1:["Add Book",addBook],2:["Display Books",displayBooks],3:["Remove Book",removeBook],4:["Search Book",searchBook],5:["Delete Book",deleteBook],6:["Update Book",updateBook],7:["Return To Main Menu"]}
def menu():
    while True:
        choice = main_menu("Books Menu",booksMenuOptions,menuSpacing)
        if(choice == "Invalid Input"):
            invalidInput()
        elif(choice == 7):
            break
        else:
            booksMenuOptions[choice][1]()
            divider()
