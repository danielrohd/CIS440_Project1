import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mysql import connector
import userclass
import event_class

from AppUI import Ui_MainWindow


def get_user_from_database(enteredUsername, enteredPassword):
    """Creates a user from the database"""
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor()
    query = f"SELECT first_name, last_name, username, password, email FROM Users WHERE username='{enteredUsername}' " \
            f"and password='{enteredPassword}' "
    cursor.execute(query)

    for first_name, last_name, username, password, email in cursor:
        if username == enteredUsername:
            temp_user = userclass.User(first_name, last_name, username, password, email)
            cnx.close()
            return temp_user

        else:
            cnx.close()
            return -1


def get_host_events_from_database(host):
    """Gets event objects from database and creates a list of all events with given host"""
    event_list = []
    cnx = connector.connect(user='fall2021group5', password='group5fall2021',
                            host='107.180.1.16',
                            database='cis440fall2021group5')
    cursor = cnx.cursor()

    query = f"SELECT title, date, location, host FROM Events where host='{host}'"
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


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)

        self.ui.loginbutton.clicked.connect(self.clickedLogin)
        self.ui.tosignup.clicked.connect(self.goSignUp)
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

            # reset text boxes to be blank
            self.ui.username.setText("")
            self.ui.password.setText("")

            # goes to event window once successfully logged in
            # can go to a different window, just did that to show the user it was successful
            self.goEvent()

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


friends = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

##user = get_user_from_database('danielrohd', 'password123')
##print(user.email)
