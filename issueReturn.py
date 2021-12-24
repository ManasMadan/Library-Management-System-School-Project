from utils import *

def issueBook():
    print("Issue Book")
def displayIssuedBooks():
    print("Display Issued Books")
def returnIssuedBooks():
    print("Return Issued Books")

issueReturnBookMenuOptions = {1:["Issue Book",issueBook],2:["Display Issued Books",displayIssuedBooks],3:["Return Issued Books",returnIssuedBooks],4:["Return To Main Menu"]}
def menu():
    while True:
        choice = main_menu("Issue Return Menu",issueReturnBookMenuOptions,menuSpacing)
        if(choice == "Invalid Input"):
            invalidInput()
        elif(choice == 4):
            break
        else:
            issueReturnBookMenuOptions[choice][1]()
            divider()