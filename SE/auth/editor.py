import auth

auth.authenticator.add_user("joe", "joepassword")
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")
auth.authorizor.permit_user("change program", "joe")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
        "adduser": self.add_user,
        "login": self.login,
        "addpermission": self.add_permission,
        "permituser": self.permit_user,
        "test": self.test,
        "change": self.change,
        "quit": self.quit
        }

    def add_user(self):
        username = input("username: ")
        password = input("password: ")
        try:
            auth.authenticator.add_user(username,password)
        except auth.UsernameAlreadyExist:
            print("The name existed already")
        except auth.PasswordTooShort:
            print("Password is too short")
        # else:
        #     auth.authenticator.users.update(add_user)

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username,password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def add_permission(self):
        perm_name = input("Permission: ")
        try:
            auth.authorizor.add_permission(perm_name)
        except auth.PermissionError:
            print("Please enter a new one, your permission already existed")
        else:
            return True

    def permit_user(self):
        perm_name = input("Permission: ")
        username = input("Belong to: ")
        try:
            auth.authorizor.permit_user(perm_name,username)
        except auth.PermissionError:
            print("Permission does not exist")
        except auth.InvalidUsername:
            print("No such username")

    def is_permitted(self,permission):
        try:
            auth.authorizor.check_permission(permission,self.username)
        except auth.NotLogginError as e:
            print("{} is logged in". format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username,permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now ...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now ...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
    Please enter a command:
    \tadduser\t\t\tAdd User
    \tlogin\t\t\tLogin
    \taddpermission\t\tAdd Permission
    \tpermituser\t\tPermit User
    \ttest\t\t\tTest the program
    \tchange\t\t\tChange the program
    \tquit\t\t\tQuit
    """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print ("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")

Editor().menu()
