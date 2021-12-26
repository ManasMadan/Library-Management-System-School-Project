# Importing All Functions from Utils Python File
from utils import *
# Importing Books Python File
import books
# Importing Members Python File
import members
# Importing Issues/Return Python File
import issueReturn

# Running The Below Code Only If The File Is Not Been Imported
if __name__ == "__main__":
    # Creating The Menu Options Dictionary
    mainMenuOptions = {
        1:["Book Management",books.menu],
        2:["Members Management",members.menu],
        3:["Issue / Return Book",issueReturn.menu],
        4:["Exit"]
    }
    # Running The Show Menu Function From Utils File On The Main Menu Options Dictionary
    showMenu("Main Menu",mainMenuOptions,menuSpacing) # Passing Main Menu as Menu Title and Menu Spacing from utils file to center the main menu heading