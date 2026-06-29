class User:
    __password = "12345"
    def __init__(self,name,email,username):
        self.name = name
        self.email = email
        self.username = username
        self.age = 14
    
    def getPassword(self):
        print(self.__password)


user1 = User("Bob","bob123@gmail.com","Bob67")
print(user1.name)
print(user1.email)
print(user1.username)

print(user1.getPassword())

#hidden variables cant be accessed directly
# print(user1.__password)