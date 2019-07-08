import datetime

user_id = 0

class User:

    def __init__(self,name,password):
        self.name = name
        self.password = password
        global user_id
        user_id += 1
        self.id = user_id
        self.post=[]

    def create_post(self):
        # print("Create")
        headline = input("Please create a headline: ")
        content = input ("Please input the content: ")
        self.post.append(headline)
        print(self.post)
        # self.post = post

    def match_headline(self,filter):
        # print("yes")
        # print("filter:", filter)
        # print("post:", self.post)
        if filter in self.post:
            return True
        # count_headline = []
        # for filter in self.post.headline:
        #     print("There are {0} results has a relation headline".format(filter))

    def delete(self,headline):
        if headline in self.post:
            self.post.remove(headline)
            print(self.post)
            print("The headline has been removed")

    def replace_headline(self):
        print("replace headline")
        old = input("What do you want to replace?")
        new = input("Replace by: ")
        # print(self.post[:])
        self.post[:] = [o.replace(old, new) for o in self.post]
        print(self.post)

    def find_headline(self):
        pass



# user_1 = User('thang', 321)
# user_1.create_post()
# user_1.create_post()
# user_1.create_post()
# # user_thang.match_headline("abc")
# # user_thang.modify_headline()
# user_1.replace_headline()


# print(admin_hoa.username)
# print(admin_thang.id)
# print(admin_thang.password)
# print(type(admin_thang.password))


# post_id = 0
#
class Post:

    def __init__(self,healine,content):
        self.headline = headline
        self.content = content
        global post_id
        post_id += 1
        self.id = post_id
        self.datetime = datetime.datetime.now()

# first_post = post('How to navigate the world')
# second_post = post('How design makes you happy')


# print(first_post.memo)
# print(first_post.id)
# print(first_post.datetime.strftime("%X"))
#
# print(second_post.memo)
# print(second_post.id)
# print(second_post.datetime.strftime("%X"))

# admin_hoa = admin('hoa', 123)
# print('HOa insert')
# admin_hoa.create_post()
# admin_hoa.create_post()
# print('Thang insert')
# admin_thang.create_post()
#
# print(admin_hoa.post[0].memo)
# print(admin_hoa.post[1].memo)
# print(admin_thang.post[0].memo)

# print('test')
# list = ['abc', ' 466', 'design']
# filter="abc"
# print(filter in list)
