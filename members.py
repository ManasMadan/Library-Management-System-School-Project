from utils import *

def addMember():
    print("Add Member")
def displayMembers():
    print("Display Members")
def searchMember():
    print("Search Members")
def deleteMember():
    print("Delete Member Record")
def updateMember():
    print("Update Member Record")

membersMenuOptions = {1:["Add Member",addMember],2:["Display Members",displayMembers],3:["Search Members",searchMember],4:["Delete Member",deleteMember],5:["Update Member",updateMember],6:["Return To Main Menu"]}
def menu():
    while True:
        choice = main_menu("Members Menu",membersMenuOptions,menuSpacing)
        if(choice == "Invalid Input"):
            invalidInput()
        elif(choice == 6):
            break
        else:
            membersMenuOptions[choice][1]()
            divider()
