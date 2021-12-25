from utils import *
import books
import members
import issueReturn

if __name__ == "__main__":
    mainMenuOptions = {1:["Book Management",books.menu],2:["Members Management",members.menu],3:["Issue / Return Book",issueReturn.menu],4:["Exit"]}
    # TEMP CODE START
    members.menu()
    # TEMP CODE END
    showMenu("Main Menu",mainMenuOptions,menuSpacing)