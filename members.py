from utils import *
from datetime import date
from prettytable import PrettyTable

def addMember():
    try:
        USER_NAME,USER_PASSWORD,DATE_OF_REGISTRATION = input(f"{Colors.OKCYAN}Enter User Name : "),input(f"Enter User Password : {Colors.ENDC}"),date.today()

        if(len(USER_NAME) < 4 or len(USER_PASSWORD) < 4):
            raise Exception(f"{Colors.FAIL}Invalid Input{Colors.ENDC}")

        USER_PASSWORD = hashPassword(USER_PASSWORD)

        query = "INSERT INTO members VALUES (%s, %s, %s);"
        data = (USER_NAME,USER_PASSWORD,DATE_OF_REGISTRATION)

        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Added")
    except:
        clearScreen()
        print("Invalid Input")

def displayMembers():
    try:
        query = "select * from members;"
        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query)

        x = PrettyTable()
        x.field_names = ["User Name","Date Of Registation"]

        for i in Cursor:
            dateString = date.strftime(i[2],"%d-%m-%Y")
            x.add_row([i[0],dateString])
        
        print(x)
        Cursor.close()
        cnx.close()

    except Exception as err:
        print(handleSQLException(err))

def searchMember():
    try:
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)

        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        x = PrettyTable()
        x.field_names = ["User Name","Date of Registation"]

        found = False
        for i in Cursor:
            dateString = date.strftime(i[2],"%d-%m-%Y")
            data = [i[0],dateString]
            x.add_row(data)
            found = True
        
        if(not found):
            x.add_row(["No User","Record Found"])

        print(x)
        Cursor.close()
        cnx.close()

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)

def deleteMember():
    try:
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")
        query = 'delete from Members where username=%s;'
        data = (USER_NAME,)
        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Deleted")
    except:
        clearScreen()
        print("Invalid Input")

def updateMemberPassword():
    try:
        USER_NAME = input(f"{Colors.OKCYAN}Enter User Name : {Colors.ENDC}")
        query = 'select * from members where username = %s;'
        data = (USER_NAME,)

        cnx = connection.MySQLConnection(user=sqlData.SQL_USERNAME,password=sqlData.SQL_PASSWORD,host='localhost',database=sqlData.DATABASE_NAME)
        Cursor = cnx.cursor()
        Cursor.execute(query,data)
        
        x = PrettyTable()
        x.field_names = ["User Name","Date Of Registation"]

        found = False
        for i in Cursor:
            USER_PASSWORD = i[1]
            dateString = date.strftime(i[2],"%d-%m-%Y")
            data = [i[0],dateString]
            x.add_row(data)
            found = True

        if(not found):
            x.add_row(["No User","Record Found"])
            print(x)
            return

        print(x)

        Cursor.close()
        cnx.close()

        OLD_USER_PASSWORD = input(f"{Colors.OKCYAN}Enter Your Old Password : {Colors.ENDC}")

        if(not checkPassword(OLD_USER_PASSWORD, USER_PASSWORD)):
            clearScreen()
            raise Exception(f"{Colors.FAIL}Wrong Password{Colors.ENDC}")
        
        USER_PASSWORD = input(f"{Colors.OKCYAN}Enter New User Password : {Colors.ENDC}")
        
        if(len(USER_PASSWORD) < 4):
            raise Exception(f"{Colors.FAIL}Invalid Input{Colors.ENDC}")

        USER_PASSWORD = hashPassword(USER_PASSWORD)
        
        query = 'UPDATE members set password=%s where username=%s'
        data = (USER_PASSWORD,USER_NAME)
        
        res = executeSQLCommitQuery(query,data)
        clearScreen()
        if(type(res) == str):
            print("Error : ", res)
        else:
            print("Member Password Updated")

    except Exception as err:
        try:
            print(handleSQLException(err))
        except:
            print(err)

def menu():
    membersMenuOptions = {1:["Add Member",addMember],2:["Display Members",displayMembers],3:["Search Members",searchMember],4:["Delete Member",deleteMember],5:["Update Member Password",updateMemberPassword],6:["Return To Main Menu"]}
    showMenu("Members Menu",membersMenuOptions,menuSpacing)
