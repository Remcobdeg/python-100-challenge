class User:
    def __init__(self, user_id, username, followers = 0, following = 0):
        print("new User created")
        # creating a Class constructor (ie, initializing starting values)
        # 'self' is the object that is being created
        # everything here will be run once a class instance is created
        self.id = user_id
        self.username = username
        self.followers = followers #using a default value
        self.following = following #using a default value

    def follow(self, user):
        # a method
        # always needs the 'self' so it knows the object that called it
        # if we decide to follow someone
        user.followers += 1
        self.following += 1

user_1 = User('001', 'Remco')
user_2 = User('002', 'Lenia', followers = 10)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
