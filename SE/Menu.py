import sys

from admin import User

class Menu:
    def __init__(self):
        self.user = []
        self.adminChoices = {
            "1": self.create_user,
            "2": self.show_user,
            "3": self.quit
            }
            

    def create_user(self):
        name = input("Please input your name: ")
        password = input('Please input the password: ')
        self.user.append(User(name,password))

    def show_user(self):
        # print(*self.user[:].name)
        for x in range(len(self.user)):
            print (self.user[x].name)


    def quit(self):
        print("Thank you!!!")
        username = input("username: ")
        password = input("password: ")
        sys.exit(0)

    def modify_headline(self):
        modify = input("Which headline do you want to modify?")
        if (self.User.match_headline(modify) == True):
            replace_by = input("Please input ")
        else:
            print("There's no such headline")

    def DisplayMenuAdmin(self):
        print("""
        Notebook menu
        1. Create user
        2. Show user
        3. Quit
        """)


    def run(self):
        while True:
            AdminName = 'SE'
            AdminPassword = '000'
            username = input("Username: ")
            password = input("Password: ")
            if ((username == AdminName) and (password == AdminPassword)):
                self.DisplayMenuAdmin()
                choice = input("Enter an option: ")
                action = self.adminChoices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid choice".format(choice))



if __name__ == "__main__":
    # test = Notebook()
    # print(type(test.notes))
    Menu().run()
