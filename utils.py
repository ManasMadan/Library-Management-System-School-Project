class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

menuSpacing = "          "

def divider():
    print(f"{Colors.OKGREEN}=============================={Colors.ENDC}")

def invalidInput():
    print(f"{Colors.FAIL}Invalid Input Enter A Choice From the Menu Above{Colors.ENDC}")
    divider()


def main_menu(menuTitle,menuOptions,menuSpacing):
    print(f"{Colors.HEADER}{menuSpacing}{menuTitle} {Colors.ENDC}")
    divider()

    for choice,statement in menuOptions.items():
        print(f"{Colors.OKBLUE}{Colors.BOLD}{choice} - {statement[0]}{Colors.ENDC}")
    
    try:
        choice = int(input("Enter Choice : "))
        divider()
        if(choice >= 1 and choice <= len(menuOptions.keys())):
            return choice
        else:
            return "Invalid Input"
    
    except:
        return "Invalid Input"

