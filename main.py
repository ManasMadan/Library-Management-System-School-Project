from utils import *
import books
import members
import issueReturn

mainMenuOptions = {1:["Book Management",books.menu],2:["Members Management",members.menu],3:["Issue / Return Book",issueReturn.menu],4:["Exit"]}

if __name__ == "__main__":
    while True:
        choice = main_menu("Main Menu",mainMenuOptions,menuSpacing)
        if(choice == "Invalid Input"):
            invalidInput()
        elif(choice == 4):
            break
        else:
            mainMenuOptions[choice][1]()
            divider()
