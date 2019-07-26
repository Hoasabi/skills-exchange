class EvenOnly(list):
    def append(self, integer):
        # if not isinstance(integer, int):
        #     raise TypeError("Only integers can be added")
        # if integer % 2:
        #     raise ValueError("Only even numbers can be added")
        super().append(integer)
# e = EvenOnly()
# e.append(103)
# print(e)
# e1 = []
# e1.append(123)
# print(e1)

def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print('No 13')
        raise
# funny_division3(13)

# try:
#     raise ValueError("This is an argument")
# except ValueError as e:
#     print("The exception arguments were", e.args)


# import random
#
#
# some_exceptions = [ValueError, TypeError, IndexError, None]
# try:
#     choice = random.choice(some_exceptions)
#     print("raising {}".format(choice))
#     if choice:
#         raise choice("An error")
# except ValueError:
#     print("Caught a ValueError")
# except TypeError:
#     print("Caught a TypeError")
# except Exception as e:
#     print("Caught some other error: {}".format(e.__class__.__name__))
# else:
#     print("This code called if there is no exception")
# finally:
#     print("This cleanup code is always called")

###############Case study chap4############
import hashlib

class User:
    def __init__(self,username, password):
        self.username = username
        self.password = self._encrypted_pw(password)
        self.is_logged_in = False

    def _encrypted_pw(self, password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self,password):
        encrypted = self._encrypted_pw(password)
        return encrypted == self.password

# hoa = User("hoa",'12345')
# print(hoa.password)
# print(hoa.check_password('2345'))



class Authenticator():
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExist(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
            # print(self.users[username])
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username,user)

        user.is_logged_in = True
        return True

    def is_logged_in(self,username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
# hoa = User("hoa",'12345')

# # auth.add_user("hoa","ahdbeelg")
# auth.login("hoang",'123456789')
# auth.login("hoa",'1234kfht')

class Authorizor:
    def __init__(self,authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self,perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self,perm_name,username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self,perm_name,username):
        if not self.authenticator.is_logged_in(username):
            raise NotLogginError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

class AuthException(Exception):
    def __init__(self,username, user = None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExist(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotLogginError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

class PermissionError(Exception):
    pass



authenticator = Authenticator()
authorizor = Authorizor (authenticator)

# auto = Authorizor(authenticator)
# # auto.add_permission('activity1')
# auto.authenticator.add_user("hoa","hoapassword")
# auto.authenticator.add_user("quy","quypassword")
# # print(auto.authenticator.users)
#
# # auto.authenticator.add_user('hoa','hoapassword')
#
# # auto.authorizor.add_permission('paint')
# # auto.authorizor.check_permission('paint',"hoa")
# # print('aaaaaaaaa')
#
# # ########################PHAN TEST NGAY 25/7
# auto.authenticator.login('hoa','hoapassword')
# auto.authenticator.is_logged_in("hoa")
# auto.add_permission('paint')
# print(auto.permissions)
# # auto.check_permission('paint','hoa')
# auto.permit_user('paint','hoa')
# auto.check_permission('paint','hoa') #chua check duoc not permitted error
# ########################


# print(auto.perm_set)
# print(auto.permissions)
# auto.add_permission('activity1')
# print(auto.permissions)
# auto.permit_user('activity1','hoa')
# auto.permit_user('activity2','hoa')
# print(auto.permissions)
