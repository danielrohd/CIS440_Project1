import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5.QtWidgets import QTableWidget
from mysql import connector
import userclass
import event_class
import datetime


from AppUI import Ui_MainWindow

# this is the user account variable, gets set to a user object upon login/account creation
user_account = 0
# this is a list of usernames that are friends of the user
friends = []
# list of usernames that have pending requests for the user to respond to
pending_friends = []
# list of usernames who have mutual friends with the user
friends_of_friends = []
# list of all events that the user can see in their feed
available_events = []


def get_user_from_database(enteredUsername, enteredPassword):
    """Creates a user from the database"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
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
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor()

    query = f"SELECT eventID, title, date, location, host FROM Events WHERE host='{host}'"
    cursor.execute(query)

    for eventID, title, date, location, host in cursor:
        if title is None:
            # this needs to properly handle if host has no events
            cnx.close()
            return 0
        else:
            temp_event = event_class.Event(eventID, title, date, location, host)
            event_list.append(temp_event)
            cnx.close()

    return event_list


def add_account_to_database(f_name, l_name, username, pw, email):
    """Function can be used to add a user to the database after an account has been created"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
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
                            host='107.180.1.16', port = '3306',
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
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    query = f'select username1, username2, status from Friends where ' \
            f'username2 = "{user_account.username}" and status = "Pending"'
    cursor.execute(query)

    for username1, username2, status in cursor:
        pending_friends.append(username1)
    cnx.close()


def send_friend_request(entered_username):
    """Sends a friend request to the user entered if the username exists and returns 1,
    returns 0 if the username does not exist, and returns 2 if the request has already been sent"""
    global user_account
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    exists = does_user_exist(entered_username)

    # checking if friend request has been sent previously
    check_query = f"SELECT username1, username2 FROM Friends WHERE " \
                  f"((username1 = '{user_account.username}' and username2 = '{entered_username}') or " \
                  f"(username1 = '{entered_username}' and username2 = '{user_account.username}'))" \
                  f"and status != 'Denied'"
    cursor.execute(check_query)
    length = cursor.rowcount
    # if length = 0, that means that these users do not already have a pending or accepted request
    # if length is more than 0, the request is already pending/accepted and wont be sent again
    if length != 0:
        cnx.close()
        return 2

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
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    if accepted:
        query = f"UPDATE cis440fall2021group5.Friends SET status = 'Accepted'" \
                f"WHERE username1 = '{friend_username}' and username2 = '{user_account.username}'"
    else:
        query = f"UPDATE cis440fall2021group5.Friends SET status = 'Denied'" \
                f"WHERE username1 = '{friend_username}' and username2 = '{user_account.username}'"

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_friend(friend_username):
    """Lets user remove friends that are on their friends list"""
    global friends, user_account
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
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
                            host='107.180.1.16', port = '3306',
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


def find_available_events():
    """Finds all events that were created by the user, their friends, and friends of friends"""
    global available_events
    available_events = []
    connections = friends + friends_of_friends
    connections.append(user_account.username)
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)
    for f in connections:
        query = f"SELECT eventID, title, date, location, host FROM Events WHERE host = '{f}'"
        cursor.execute(query)
        length = cursor.rowcount
        if length > 0:
            for eventID, title, date, location, host in cursor:
                temp_event = event_class.Event(eventID, title, date, location, host)
                temp_event.guests = get_guest_list(eventID)
                # if any(x.event_id == eventID for x in available_events):
                    # available_events.append(temp_event)
                if temp_event not in available_events:
                    available_events.append(temp_event)
    available_events.sort(key=lambda x: x.date)


def get_guest_list(event_id):
    """Gets and returns the guest list for a specific event"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    query = f"SELECT userID, eventID FROM Guests WHERE eventID = '{event_id}'"
    cursor.execute(query)
    temp_guest_list = []

    for userID, eventID in cursor:
        temp_guest_list.append(userID)

    return temp_guest_list


def modify_guest_list(event_id):
    """Either adds the user as a guest and returns 1, or removes them if they are already a guest and returns 0"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    check_query = f"SELECT * from Guests WHERE userID = '{user_account.username}' and eventID = '{event_id}'"
    cursor.execute(check_query)
    length = cursor.rowcount

    if length == 0:
        query = f"INSERT INTO Guests (userID, eventID) VALUES ('{user_account.username}', '{event_id}')"
        cursor.execute(query)

        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    elif length == 1:
        query = f"DELETE FROM Guests WHERE userID = '{user_account.username}' and eventID = '{event_id}'"
        cursor.execute(query)

        cnx.commit()
        cursor.close()
        cnx.close()
        return 0


def create_event(title, date, location):
    """Lets users create an event and upload it to the database"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port = '3306',
                            database='cis440fall2021group5')
    cursor = cnx.cursor(buffered=True)

    creation_query = f"INSERT INTO Events (title, date, location, host) VALUES" \
                     f"('{title}', '{date}', '{location}', '{user_account.username}')"
    cursor.execute(creation_query)

    cnx.commit()
    cursor.close()
    cnx.close()


def does_user_exist(username):
    """Checks to see if a username already exists"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16', port='3306',
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
    find_available_events()


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

        self.ui.addEventButton.clicked.connect(self.goEventCreation)
        self.ui.backToEventsButton.clicked.connect(self.goEvent)
        self.ui.backToLoginButton.clicked.connect(self.logOut)
        self.ui.publishEventButton.clicked.connect(self.createEvent)
        self.ui.registerEventButton.clicked.connect(self.registerEvent)
        self.ui.acceptRequestButton.clicked.connect(self.acceptRequest)
        self.ui.declineRequestButton.clicked.connect(self.denyRequest)

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

        self.ui.eventTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.stackedWidget.setCurrentWidget(self.ui.event_page)
        self.ui.suggested_friend_list_widget.clear()
        self.ui.flist_widget.clear()
        find_available_events()

        self.ui.eventTable.setRowCount(len(available_events))
        row = 0

        for event in available_events:

            self.ui.eventTable.setItem(row, 0, QTableWidgetItem(event.title))

            date = str(event.date)
            self.ui.eventTable.setItem(row, 1, QTableWidgetItem(date))
            self.ui.eventTable.setItem(row, 2, QTableWidgetItem(event.location))
            self.ui.eventTable.setItem(row, 3, QTableWidgetItem(event.host))
            row += 1


    def goFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.friends_page)
        self.ui.flist_widget.addItems(friends)
        self.ui.suggested_friend_list_widget.addItems(friends_of_friends)
        self.ui.uname_addfriend.setText("")

    def goNoti(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.notis_page)
        self.ui.suggested_friend_list_widget.clear()
        self.ui.flist_widget.clear()
        self.ui.uname_addfriend.setText("")

    def goSignUp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up_page)

    def createEvent(self):
        entered_location = self.ui.location.text()
        entered_date_time = self.ui.dateTime.text()
        entered_description = self.ui.description.text()

        print(entered_location)
        print(entered_date_time)
        print(entered_description)

        create_event(entered_description, entered_date_time, entered_location)

        self.ui.location.setText("")
        self.ui.dateTime.setText("")
        self.ui.description.setText("")
        self.goEvent()

    def registerEvent(self):

        selectedRow = self.ui.eventTable.currentIndex().row()
        eventId = available_events[selectedRow].event_id
        result = modify_guest_list(eventId)
        if result == 1:
            print('registered')
            self.ui.add_event_header.setText("You are now registered")
            # say registered
        elif result == 0:
            print('unregistered')
            self.ui.add_event_header.setText("You are now not registered for that event")
            # say unregistered

    def acceptRequest(self):
        print('hey')


    def denyRequest(self):
        print('hey');



    def logOut(self):
        global user_account, friends, pending_friends, friends_of_friends
        user_account = 0
        friends = []
        pending_friends = []
        friends_of_friends = []
        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)

    def goEventCreation(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.create_event_page)

    def addFriendButton(self):

        usernameEntered = self.ui.uname_addfriend.text()
        result = send_friend_request(usernameEntered)
        ##print(result)
        if result == 1:
            self.ui.add_friend_header.setText("Friend Request Sent!")

        elif result == 2:
            self.ui.add_friend_header.setText("A request already exists with that user!")
            self.ui.uname_addfriend.setText("")

        else:
            self.ui.add_friend_header.setText("This isn't a valid username, try again!")
            self.ui.uname_addfriend.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

# user_account = get_user_from_database('danielrohd', 'password123')
# create_friends_list()
# print(friends)

# add_account_to_database('test', 'user', 'testuser', 'password321', 'user@user.com')
