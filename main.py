import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from AppUI import Ui_MainWindow


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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
