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

def menu():
    membersMenuOptions = {1:["Add Member",addMember],2:["Display Members",displayMembers],3:["Search Members",searchMember],4:["Delete Member",deleteMember],5:["Update Member",updateMember],6:["Return To Main Menu"]}
    showMenu("Members Menu",membersMenuOptions,menuSpacing)
