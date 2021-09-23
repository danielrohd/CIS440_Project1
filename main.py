import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import mysql.connector
import userclass
import event_class


from AppUI import Ui_MainWindow


def get_user_from_database(username, password):
    """Creates a user from the database"""
    cnx = mysql.connector.connect(user='fall2021group5', password='group5fall2021',
                                  host='107.180.1.16',
                                  database='cis440fall2021group5')
    cursor = cnx.cursor()
    query = f"SELECT first_name, last_name, username, password, email FROM Users WHERE username='{username}' " \
            f"and password='{password}' "
    cursor.execute(query)

    for first_name, last_name, username, password, email in cursor:
        if first_name is None:
            # this needs to be fixed to control for if account does not exist
            cnx.close()
            return 0
        else:
            temp_user = userclass.User(first_name, last_name, username, password, email)
            cnx.close()
            return temp_user


def get_host_events_from_database(host):
    """Gets an event object from database and creates an event object"""
    cnx = mysql.connector.connect(user='fall2021group5', password='group5fall2021',
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
            cnx.close()
            return temp_event


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.login1)

        self.ui.loginbutton.clicked.connect(self.goEvent)
        self.ui.events_tab.clicked.connect(self.goEvent)
        self.ui.friends_tab.clicked.connect(self.goFriends)
        self.ui.noti_tab.clicked.connect(self.goNoti)

    def show(self):
        self.main_win.show()

    def goEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.events)

    def goFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.friends)

    def goNoti(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.notifications)


friends = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

user = get_user_from_database('danielrohd', 'password123')
print(user.email)
