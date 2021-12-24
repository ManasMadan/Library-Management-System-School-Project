from utils import *

def issueBook():
    print("Issue Book")
def displayIssuedBooks():
    print("Display Issued Books")
def returnIssuedBooks():
    print("Return Issued Books")

def menu():
    issueReturnBookMenuOptions = {1:["Issue Book",issueBook],2:["Display Issued Books",displayIssuedBooks],3:["Return Issued Books",returnIssuedBooks],4:["Return To Main Menu"]}
    showMenu("Issue Return Menu",issueReturnBookMenuOptions,menuSpacing)