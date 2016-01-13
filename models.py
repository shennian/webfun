from db import mongo
from flask import request


class User():

    db = mongo.users.posts

    def __init__(self, name, password, email=None):
        self.name = name
        self.password = password
        self.email = email

    def checkout(self):
        return self.db.find_one({"name": self.name, "password": self.password}) is not None

    def sigup(self):
        pass

    def to_json(self):
        id = self.create_id()

    def create_id(self):
        pass


class Group():

    db = mongo.group.posts

    def __init__(self, name):
        self.name = name


class Form:
    def __init__(self, *args):
        self.keywords = args

    def parse_request(self):
        for keyword in self.keywords:
            try:
                setattr(Form, keyword, request.form[keyword])
            except:
                setattr(Form, keyword, None)

    def submit(self):
        for keyword in self.keywords:
            if getattr(Form, keyword, None) is None:
                return False
        return True


class LoginForm(Form):
    def __init__(self):
        Form.__init__(self, "username", "password")


class RegisterForm(Form):
    def __init__(self):
        Form.__init__(self, "email", "password")


class UserInfoForm(Form):
    def __init__(self):
        # the items of UserInfoForm has not been decided
        Form.__init__(self, "username", "gender", "city")






























class LoginForm():
    def __init__(self):
        try:
            self.username = request.form['username']
            self.password = request.form['password']
        except:
            self.username = None
            self.password = None

    def submit(self):
        return self.username is not None and self.password is not None


class RegisterForm():
    def __init__(self):
        try:
            self.email = request.form['email']
            self.password = request.form['password']
        except:
            self.email = None
            self.password = None

    def submit(self):
        return self.email is not None and self.password is not None


class UserInfoForm():
    def __init__(self):
        pass

    def submit(self):
        pass

































