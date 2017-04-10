import datetime
import time
import json
import os
#from pathlib import Path


filepath = 'A:/Desktop/myProject/Project Files/userBook.txt'

class createUser():
    userBook = {}

    name = ""
    last_name = ""
    password_type = ""

    username = ""
    password = ""

    PAO1_person = ""
    PAO1_action = ""
    PAO1_object = ""
    PAO1_full = ""

    PAO2_person = ""
    PAO2_action = ""
    PAO2_object = ""
    PAO2_full = ""

    number = ""
    symbol = ""

    setup_time = ""
    first_login = ""
    last_login = ""

    def __init__(self, n, l, pt):
        #print("New User!")
        self.name = n
        self.lastName = l
        self.passwordType = pt

        self.username = self.name + self.lastName + self.passwordType

    def save(self):
        #print("Saving user")

        self.last_login = self.first_login,
        #my_file = Path(filepath)
        #if my_file.is_file():
        if (os.path.isfile(filepath)):
            if(os.stat(filepath).st_size != 0):
                with open(filepath, "r") as f:
                    oldfile = f.read()
                    oldbook = json.loads(oldfile)

                    if self.username in oldbook:
                        print("there's already a user named "+ self.username)
                    else:
                        print('no user named ' + self.username)

        self.userBook[self.username] = {
            'name:': self.name,
            'last name': self.lastName,
            'password type': self.passwordType,
            'password': self.password,
            'PAO1_person': self.PAO1_person,
            'PAO1_action': self.PAO1_action,
            'PAO1_object': "JonnyBoTest",#self.PAO1_object,
            'PAO1_full': self.PAO1_full,
            'PAO2_person': self.PAO2_person,
            'PAO2_action': self.PAO2_action,
            'PAO2_object': self.PAO2_object,
            'PAO2_full': self.PAO2_full,
            'number': self.number,
            'symbol': self.symbol,
            'setup time': self.setup_time,
            'first login': self.first_login,
            'last login': self.last_login
        }

        with open(filepath, "w") as f:
            newbook = json.dumps(self.userBook)
            f.write(newbook)

        #json.dumps(userBook)

if __name__== "__main__":
    myuser = createUser("Jonny", "Bo", "Test")
    myuser.save()





