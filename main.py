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
# this is a list of usernames, that are friends of the user
friends = []

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

    check_account = f'SELECT username FROM Users WHERE username="{username}"'
    cursor.execute(check_account)

    length = cursor.rowcount
    if length == 0:
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
        return 0



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

        self.ui.events_tab_2.clicked.connect(self.goEvent)
        self.ui.friends_tab_2.clicked.connect(self.goFriends)
        self.ui.noti_tab_2.clicked.connect(self.goNoti)

        self.ui.events_tab_3.clicked.connect(self.goEvent)
        self.ui.friends_tab_3.clicked.connect(self.goFriends)
        self.ui.noti_tab_3.clicked.connect(self.goNoti)

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
            # reset text boxes to be blank
            self.ui.username.setText("")
            self.ui.password.setText("")

            # goes to event window once successfully logged in
            # can go to a different window, just did that to show the user it was successful
            self.goEvent()

    def clickedCreateAccount(self):
        global user_account
        username = self.ui.SU_username.text()
        pw = self.ui.SU_password.text()
        first = self.ui.SU_firstname.text()
        last = self.ui.SU_lastname.text()

        result = add_account_to_database(first, last, username, pw, "testemail@email.com")
        if result != 0:
            user_account = result
            self.ui.SU_username.setText("")
            self.ui.SU_password.setText("")
            self.ui.SU_firstname.setText("")
            self.ui.SU_lastname.setText("")
            self.goEvent()
        else:
            self.ui.SU_username.setText("")
            self.ui.SU_password.setText("")
            self.ui.SU_firstname.setText("")
            self.ui.SU_lastname.setText("")
            # maybe make a pop-up that tells the user that the username is taken already

    def show(self):
        self.main_win.show()

    def goEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.event_page)

    def goFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.friends_page)

    def goNoti(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.notis_page)

    def goSignUp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

# user = get_user_from_database('testuser', 'password321')
# print(user.email)

# add_account_to_database('test', 'user', 'testuser', 'password321', 'user@user.com')

