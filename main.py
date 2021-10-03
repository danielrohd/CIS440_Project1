import sys
import datetime
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mysql import connector
import userclass
import event_class

from AppUI import Ui_MainWindow

# this is the user account variable, gets set to a user objet upon login/account creation
user_account = 0
# this is a list of usernames that are friends of the user
friends = []
# list of usernames that have pending requests for the user to respond to
pending_friends = []
# list of usernames who have mutual friends with the user
friends_of_friends = []


def get_user_from_database(enteredUsername, enteredPassword):
    """Creates a user from the database"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor()
    query = f"SELECT first_name, last_name, username, password, email FROM Users WHERE username='{enteredUsername}' " \
            f"and password='{enteredPassword}' "
    cursor.execute(query)

    if cursor.rowcount == 0:
        cnx.close()
        return -1
    else:
        for first_name, last_name, username, password, email in cursor:
            if username == enteredUsername and password == enteredPassword:
                temp_user = userclass.User(first_name, last_name, username, password, email)
                cnx.close()
                return temp_user


def get_host_events_from_database(host):
    """Gets event objects from database and creates a list of all events with given host"""
    event_list = []
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor()

    query = f"SELECT title, date, location, host FROM Events WHERE host='{host}'"
    cursor.execute(query)

    for title, date, location, host in cursor:
        if title is None:
            # this needs to properly handle if host has no events
            cnx.close()
            return 0
        else:
            temp_event = event_class.Event(title, date, location, host)
            event_list.append(temp_event)
            cnx.close()

    return event_list


def add_account_to_database(f_name, l_name, username, pw, email):
    """Function can be used to add a user to the database after an account has been created"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    exists = does_user_exist(username)
    if not exists:
        add_query = f"INSERT INTO Users (username, password, first_name, last_name, email) VALUES" \
                    f" ('{username}', '{pw}', '{f_name}', '{l_name}', '{email}')"
        cursor.execute(add_query)

        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    else:
        # if this else executes, this means the account already exists
        # add a pop-up here that lets the user know the name is taken
        cnx.close()
        return 0


def create_friends_list():
    """This function will be run on login, and will create a username list of the user's friends"""
    global user_account, friends
    friends = []
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    query = f'select username1, username2, status from Friends where (username1 = ' \
            f'"{user_account.username}" or username2 = "{user_account.username}") and status = "Accepted"'
    cursor.execute(query)

    for username1, username2, status in cursor:
        if username1 == user_account.username:
            friends.append(username2)
        elif username2 == user_account.username:
            friends.append(username1)
    cnx.close()


def find_friend_requests():
    """Creates a list of all pending friend requests for the signed-in user"""
    global user_account, pending_friends
    pending_friends = []
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    query = f'select username1, username2, status from Friends where ' \
            f'username2 = "{user_account.username}" and status = "Pending"'
    cursor.execute(query)

    for username1, username2, status in cursor:
        pending_friends.append(username1)
    cnx.close()


def send_friend_request(entered_username):
    """Sends a friend request to the user entered if the username exists and returns 1, otherwise returns 0"""
    global user_account
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    exists = does_user_exist(entered_username)

    # checking if friend request has been sent previously
    check_query = f"SELECT username1, username2 from Friends WHERE " \
                  f"(username1 = '{user_account.username}' and username2 = '{entered_username}') or " \
                  f"(username1 = '{entered_username}' and username2 = '{user_account.username}'"
    cursor.execute(check_query)
    length = cursor.rowcount
    if length != 0:
        cnx.close()
        return 0

    if exists:
        add_query = f"INSERT INTO Friends (username1, username2, status) VALUES " \
                    f"('{user_account.username}', '{entered_username}', 'Pending')"
        cursor.execute(add_query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    else:
        cnx.close()
        return 0


def respond_to_friend_request(friend_username, accepted):
    """Accepts a friend request if accepted == True, otherwise denies"""
    global user_account
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    if accepted:
        query = f"UPDATE `cis440fall2021group5`.`Friends` SET `status` = 'Accepted'" \
                f"WHERE username1 = '{friend_username}' and username2 = '{user_account.username}'"
    else:
        query = f"UPDATE `cis440fall2021group5`.`Friends` SET `status` = 'Denied'" \
                f"WHERE username1 = '{friend_username}' and username2 = '{user_account.username}'"

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_friend(friend_username):
    """Lets user remove friends that are on their friends list"""
    global friends, user_account
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    delete_query = f"DELETE FROM `cis440fall2021group5`.`Friends` WHERE " \
                   f"(username1 = '{user_account.username}' and username2 = '{friend_username}') or " \
                   f"(username1 = '{friend_username}' and username2 = '{user_account.username}'"
    cursor.execute(delete_query)
    friends.remove(friend_username)

    cnx.commit()
    cursor.close()
    cnx.close()


def find_friends_of_friends():
    global friends, friends_of_friends
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    for f in friends:
        query = f"SELECT username1, username2, status FROM Friends where (username1 = '{f}' or username2 = '{f}') " \
                f"and status = 'Accepted'"
        cursor.execute(query)
        for username1, username2, status in cursor:
            if username1 == f and username2 not in friends_of_friends and username2 not in friends\
                    and username2 != user_account.username:
                friends_of_friends.append(username2)
            elif username2 == f and username1 not in friends_of_friends and username1 not in friends \
                    and username1 != user_account.username:
                friends_of_friends.append(username1)

    cnx.close()


def does_user_exist(username):
    """Checks to see if a username already exists"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    check_account = f'SELECT username FROM Users WHERE username="{username}"'
    cursor.execute(check_account)

    length = cursor.rowcount
    if length == 0:
        return False
    else:
        return True


def refresh_feed():
    """Calls all functions that refresh feed, such as friends, friend requests, or events"""
    create_friends_list()
    find_friend_requests()
    find_friends_of_friends()


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)

        self.ui.loginbutton.clicked.connect(self.clickedLogin)
        self.ui.tosignup.clicked.connect(self.goSignUp)
        self.ui.createaccount.clicked.connect(self.clickedCreateAccount)
        self.ui.events_tab.clicked.connect(self.goEvent)
        self.ui.friends_tab.clicked.connect(self.goFriends)
        self.ui.noti_tab.clicked.connect(self.goNoti)
        self.ui.addfriend_button.clicked.connect(self.addFriendButton)

        self.ui.events_tab_2.clicked.connect(self.goEvent)
        self.ui.friends_tab_2.clicked.connect(self.goFriends)
        self.ui.noti_tab_2.clicked.connect(self.goNoti)

        self.ui.events_tab_3.clicked.connect(self.goEvent)
        self.ui.friends_tab_3.clicked.connect(self.goFriends)
        self.ui.noti_tab_3.clicked.connect(self.goNoti)

        self.ui.log_out_button.clicked.connect(self.logOut)
        self.ui.log_out_button_2.clicked.connect(self.logOut)
        self.ui.log_out_button_3.clicked.connect(self.logOut)

    def clickedLogin(self):
        global user_account
        self.main_win.show()

        # get username and password from text boxes and compare to what is in the database
        usernameEntered = self.ui.username.text()
        passwordEntered = self.ui.password.text()
        result = get_user_from_database(usernameEntered, passwordEntered)

        if result is None:

            self.ui.username.setText("")
            self.ui.password.setText("")

            # need to add in error message below that will tell the user the password and username are wrong
            # requires adding a widget

        else:

            user_account = result
            refresh_feed()
            # reset text boxes to be blank
            self.ui.username.setText("")
            self.ui.password.setText("")

            # goes to event window once successfully logged in
            # can go to a different window, just did that to show the user it was successful
            self.goEvent()
            create_friends_list()

    def clickedCreateAccount(self):
        global user_account
        username = self.ui.SU_username.text()
        pw = self.ui.SU_password.text()
        first = self.ui.SU_firstname.text()
        last = self.ui.SU_lastname.text()
        email = self.ui.SU_email.text()

        result = add_account_to_database(first, last, username, pw, email)
        if result != 0:
            user_account = result
            refresh_feed()
            self.ui.SU_username.setText("")
            self.ui.SU_password.setText("")
            self.ui.SU_firstname.setText("")
            self.ui.SU_lastname.setText("")
            self.ui.SU_email.setText("")
            self.goEvent()
        else:
            self.ui.SU_username.setText("")
            self.ui.SU_password.setText("")
            self.ui.SU_firstname.setText("")
            self.ui.SU_lastname.setText("")
            self.ui.SU_email.setText("")
            # maybe make a pop-up that tells the user that the username is taken already

    def show(self):
        self.main_win.show()

    def goEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.event_page)

    def goFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.friends_page)
        self.ui.flist_widget.addItems(friends)
        self.ui.suggested_friend_list_widget.addItems(friends_of_friends)

    def goNoti(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.notis_page)

    def goSignUp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up_page)

    def logOut(self):
        global user_account, friends, pending_friends, friends_of_friends
        user_account = 0
        friends = []
        pending_friends = []
        friends_of_friends = []
        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)

    def addFriendButton(self):

        print('hey')
        #usernameEntered = self.ui.uname_addfriend.text()
        #result = send_friend_request(usernameEntered)
        #print(result)
        #if usernameEntered == 1:
            #print('yes')
        #else:
            #print('no')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

# user_account = get_user_from_database('danielrohd', 'password123')
# create_friends_list()
# print(friends)

# add_account_to_database('test', 'user', 'testuser', 'password321', 'user@user.com')

