# this file is to create the user class and give them certain function and attributes 

class User:
    "User class holds name,username,password,and email"

    def __init__(self,fname,lname,username,password,email):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.__password = password
        self.email = email
       
    @property
    def fname(self):
        return self.__fname.capitalize()

    @fname.setter
    def fname(self, new_name):
        self.__fname = new_name

    @property
    def lname(self):
        return self.__lname.capitalize()

    @fname.setter
    def lname(self, new_name):
        if new_name.isalpha():
            self.__lname = new_name
        else:
            self.__lname = 'Unknown'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username
       
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email


    def add_user(self, username):
        """Add user to the user list"""
        if username not in self.user_list:
            self.user_list.append(username)
            
    def remove_user(self, username):
        """Removes a guest from the guest list"""
        if username in self.user_list:
            self.user_list.remove(username)


        
       


