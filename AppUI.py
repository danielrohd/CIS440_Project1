from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 471, 511))
        self.stackedWidget.setObjectName("stackedWidget")
        self.log_in_page = QtWidgets.QWidget()
        self.log_in_page.setObjectName("log_in_page")
        self.pwordlabel = QtWidgets.QLabel(self.log_in_page)
        self.pwordlabel.setGeometry(QtCore.QRect(80, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwordlabel.setFont(font)
        self.pwordlabel.setObjectName("pwordlabel")
        self.unamelabel = QtWidgets.QLabel(self.log_in_page)
        self.unamelabel.setGeometry(QtCore.QRect(80, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unamelabel.setFont(font)
        self.unamelabel.setObjectName("unamelabel")
        self.username = QtWidgets.QLineEdit(self.log_in_page)
        self.username.setGeometry(QtCore.QRect(170, 40, 161, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.log_in_page)
        self.password.setGeometry(QtCore.QRect(170, 90, 161, 20))
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(self.log_in_page)
        self.loginbutton.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.loginbutton.setObjectName("loginbutton")
        self.tosignup = QtWidgets.QPushButton(self.log_in_page)
        self.tosignup.setGeometry(QtCore.QRect(190, 440, 111, 23))
        self.tosignup.setObjectName("tosignup")
        self.signup_pointer = QtWidgets.QLabel(self.log_in_page)
        self.signup_pointer.setGeometry(QtCore.QRect(190, 410, 151, 20))
        self.signup_pointer.setObjectName("signup_pointer")
        self.stackedWidget.addWidget(self.log_in_page)
        self.sign_up_page = QtWidgets.QWidget()
        self.sign_up_page.setObjectName("sign_up_page")
        self.SU_firstname_label = QtWidgets.QLabel(self.sign_up_page)
        self.SU_firstname_label.setGeometry(QtCore.QRect(70, 130, 111, 16))
        self.SU_firstname_label.setObjectName("SU_firstname_label")
        self.SU_lastname_label = QtWidgets.QLabel(self.sign_up_page)
        self.SU_lastname_label.setGeometry(QtCore.QRect(70, 170, 111, 16))
        self.SU_lastname_label.setObjectName("SU_lastname_label")
        self.SU_username_label = QtWidgets.QLabel(self.sign_up_page)
        self.SU_username_label.setGeometry(QtCore.QRect(70, 210, 111, 16))
        self.SU_username_label.setObjectName("SU_username_label")
        self.SU_firstname = QtWidgets.QLineEdit(self.sign_up_page)
        self.SU_firstname.setGeometry(QtCore.QRect(200, 130, 201, 20))
        self.SU_firstname.setObjectName("SU_firstname")
        self.SU_lastname = QtWidgets.QLineEdit(self.sign_up_page)
        self.SU_lastname.setGeometry(QtCore.QRect(200, 170, 201, 20))
        self.SU_lastname.setObjectName("SU_lastname")
        self.SU_username = QtWidgets.QLineEdit(self.sign_up_page)
        self.SU_username.setGeometry(QtCore.QRect(200, 210, 201, 20))
        self.SU_username.setObjectName("SU_username")
        self.SU_password_label = QtWidgets.QLabel(self.sign_up_page)
        self.SU_password_label.setGeometry(QtCore.QRect(70, 250, 111, 16))
        self.SU_password_label.setObjectName("SU_password_label")
        self.SU_password = QtWidgets.QLineEdit(self.sign_up_page)
        self.SU_password.setGeometry(QtCore.QRect(200, 250, 201, 20))
        self.SU_password.setObjectName("SU_password")
        self.SU_email_label = QtWidgets.QLabel(self.sign_up_page)
        self.SU_email_label.setGeometry(QtCore.QRect(70, 290, 101, 16))
        self.SU_email_label.setObjectName("SU_email_label")
        self.SU_email = QtWidgets.QLineEdit(self.sign_up_page)
        self.SU_email.setGeometry(QtCore.QRect(200, 290, 201, 20))
        self.SU_email.setObjectName("SU_email")
        self.createaccount = QtWidgets.QPushButton(self.sign_up_page)
        self.createaccount.setGeometry(QtCore.QRect(150, 380, 171, 23))
        self.createaccount.setObjectName("createaccount")
        self.backToLoginButton = QtWidgets.QPushButton(self.sign_up_page)
        self.backToLoginButton.setGeometry(QtCore.QRect(180, 470, 75, 23))
        self.backToLoginButton.setObjectName("backToLoginButton")
        self.account_creation_label = QtWidgets.QLabel(self.sign_up_page)
        self.account_creation_label.setGeometry(QtCore.QRect(140, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.account_creation_label.setFont(font)
        self.account_creation_label.setObjectName("account_creation_label")
        self.stackedWidget.addWidget(self.sign_up_page)
        self.event_page = QtWidgets.QWidget()
        self.event_page.setObjectName("event_page")
        self.friends_tab = QtWidgets.QPushButton(self.event_page)
        self.friends_tab.setGeometry(QtCore.QRect(10, 450, 111, 23))
        self.friends_tab.setObjectName("friends_tab")
        self.events_tab = QtWidgets.QPushButton(self.event_page)
        self.events_tab.setGeometry(QtCore.QRect(160, 450, 111, 23))
        self.events_tab.setObjectName("events_tab")
        self.noti_tab = QtWidgets.QPushButton(self.event_page)
        self.noti_tab.setGeometry(QtCore.QRect(310, 450, 111, 23))
        self.noti_tab.setObjectName("noti_tab")
        self.event_title = QtWidgets.QLabel(self.event_page)
        self.event_title.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.event_title.setFont(font)
        self.event_title.setObjectName("event_title")
        self.stackedWidget.addWidget(self.event_page)
        self.friends_page = QtWidgets.QWidget()
        self.friends_page.setObjectName("friends_page")
        self.friends_tab_2 = QtWidgets.QPushButton(self.friends_page)
        ##was 450
        self.friends_tab_2.setGeometry(QtCore.QRect(10,490, 111, 23))
        self.friends_tab_2.setObjectName("friends_tab_2")
        self.events_tab_2 = QtWidgets.QPushButton(self.friends_page)
        self.events_tab_2.setGeometry(QtCore.QRect(160,490, 111, 23))
        self.events_tab_2.setObjectName("events_tab_2")
        self.noti_tab_2 = QtWidgets.QPushButton(self.friends_page)
        self.noti_tab_2.setGeometry(QtCore.QRect(310,490, 111, 23))
        self.noti_tab_2.setObjectName("noti_tab_2")
        self.log_out_button_2 = QtWidgets.QPushButton(self.event_page)
        self.log_out_button_2.setGeometry(QtCore.QRect(340, 10, 81, 23))
        self.log_out_button_2.setObjectName("log_out_button_2")
        self.flist_title = QtWidgets.QLabel(self.friends_page)
        self.flist_title.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flist_title.setFont(font)
        self.flist_title.setObjectName("flist_title")
        self.flist_widget = QtWidgets.QListWidget(self.friends_page)
        self.flist_widget.setGeometry(QtCore.QRect(5, 41, 431, 141))
        self.flist_widget.setObjectName("flist_widget")

        self.suggested_friend_list_widget = QtWidgets.QListWidget(self.friends_page)
        self.suggested_friend_list_widget.setGeometry(QtCore.QRect(5, 250, 431, 141))
        self.suggested_friend_list_widget.setObjectName("suggested_friend_list_widget")

        self.suggested_friend_list_title = QtWidgets.QLabel(self.friends_page)
        self.suggested_friend_list_title.setGeometry(QtCore.QRect(10, 225, 181, 21))
        self.suggested_friend_list_title.setFont(font)
        self.suggested_friend_list_title.setObjectName("suggested_friend_list_title")

        self.add_friend_header = QtWidgets.QLabel(self.friends_page)
        self.add_friend_header.setGeometry(QtCore.QRect(90, 410, 351, 20))
        self.add_friend_header.setFont(font)
        self.add_friend_header.setObjectName("add_friend_header")


        self.uname_addfriend = QtWidgets.QLineEdit(self.friends_page)
        self.uname_addfriend.setGeometry(QtCore.QRect(90, 440, 151, 20))
        self.uname_addfriend.setObjectName("uname_addfriend")
        self.uname_addfriend_label = QtWidgets.QLabel(self.friends_page)
        self.uname_addfriend_label.setGeometry(QtCore.QRect(20, 440, 61, 16))
        self.uname_addfriend_label.setObjectName("uname_addfriend_label")
        self.addfriend_button = QtWidgets.QPushButton(self.friends_page)
        self.addfriend_button.setGeometry(QtCore.QRect(270, 440, 135, 23))
        self.addfriend_button.setObjectName("addfriend_button")
        self.stackedWidget.addWidget(self.friends_page)
        self.eventTable = QtWidgets.QTableWidget(self.event_page)
        self.eventTable.setGeometry(QtCore.QRect(-10, 100, 481, 281))
        self.eventTable.setObjectName("eventTable")
        self.eventTable.setColumnCount(4)
        self.eventTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(3, item)
        self.addEventButton = QtWidgets.QPushButton(self.event_page)
        self.addEventButton.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.addEventButton.setObjectName("addEventButton")
        self.stackedWidget.addWidget(self.event_page)
        self.create_event_page = QtWidgets.QWidget()
        self.create_event_page.setObjectName("create_event_page")
        self.dateTimeLabel = QtWidgets.QLabel(self.create_event_page)
        self.dateTimeLabel.setGeometry(QtCore.QRect(0, 60, 161, 21))
        self.dateTimeLabel.setObjectName("dateTimeLabel")
        self.locationLabel = QtWidgets.QLabel(self.create_event_page)
        self.locationLabel.setGeometry(QtCore.QRect(0, 110, 81, 21))
        self.locationLabel.setObjectName("locationLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.create_event_page)
        self.descriptionLabel.setGeometry(QtCore.QRect(0, 160, 81, 21))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.dateTime = QtWidgets.QLineEdit(self.create_event_page)
        self.dateTime.setGeometry(QtCore.QRect(170, 60, 201, 20))
        self.dateTime.setObjectName("dateTime")
        self.location = QtWidgets.QLineEdit(self.create_event_page)
        self.location.setGeometry(QtCore.QRect(170, 110, 201, 20))
        self.location.setObjectName("location")
        self.description = QtWidgets.QTextEdit(self.create_event_page)
        self.description.setGeometry(QtCore.QRect(170, 160, 201, 51))
        self.description.setObjectName("description")
        self.publishEventButton = QtWidgets.QPushButton(self.create_event_page)
        self.publishEventButton.setGeometry(QtCore.QRect(130, 290, 181, 31))
        self.publishEventButton.setObjectName("publishEventButton")
        self.backToEventsButton = QtWidgets.QPushButton(self.create_event_page)
        self.backToEventsButton.setGeometry(QtCore.QRect(180, 460, 75, 23))
        self.backToEventsButton.setObjectName("backToEventsButton")
        self.stackedWidget.addWidget(self.create_event_page)
        self.notis_page = QtWidgets.QWidget()
        self.notis_page.setObjectName("notis_page")
        self.friends_tab_3 = QtWidgets.QPushButton(self.notis_page)
        self.friends_tab_3.setGeometry(QtCore.QRect(10, 450, 111, 23))
        self.friends_tab_3.setObjectName("friends_tab_3")
        self.events_tab_3 = QtWidgets.QPushButton(self.notis_page)
        self.events_tab_3.setGeometry(QtCore.QRect(160, 450, 111, 23))
        self.events_tab_3.setObjectName("events_tab_3")
        self.noti_tab_3 = QtWidgets.QPushButton(self.notis_page)
        self.noti_tab_3.setGeometry(QtCore.QRect(310, 450, 111, 23))
        self.noti_tab_3.setObjectName("noti_tab_3")
        self.log_out_button_3 = QtWidgets.QPushButton(self.friends_page)
        self.log_out_button_3.setGeometry(QtCore.QRect(340, 10, 81, 23))
        self.log_out_button_3.setObjectName("log_out_button_3")
        self.noti_title = QtWidgets.QLabel(self.notis_page)
        self.noti_title.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noti_title.setFont(font)
        self.noti_title.setObjectName("noti_title")
        self.log_out_button = QtWidgets.QPushButton(self.notis_page)
        self.log_out_button.setGeometry(QtCore.QRect(340, 10, 81, 23))
        self.log_out_button.setObjectName("log_out_button")
        self.stackedWidget.addWidget(self.notis_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pwordlabel.setText(_translate("MainWindow", "Password:"))
        self.unamelabel.setText(_translate("MainWindow", "Username:"))
        self.tosignup.setText(_translate("MainWindow", "Create Account"))
        self.signup_pointer.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.loginbutton.setText(_translate("MainWindow", "Log in"))
        self.SU_firstname_label.setText(_translate("MainWindow", "First Name: "))
        self.SU_lastname_label.setText(_translate("MainWindow", "Last Name:"))
        self.SU_username_label.setText(_translate("MainWindow", "Username: "))
        self.SU_password_label.setText(_translate("MainWindow", "Password: "))
        self.createaccount.setText(_translate("MainWindow", "Create Account"))
        self.account_creation_label.setText(_translate("MainWindow", "Account Creation"))
        self.SU_email_label.setText(_translate("MainWindow", "Email: "))
        self.backToLoginButton.setText(_translate("MainWindow", "Back"))
        self.friends_tab.setText(_translate("MainWindow", "Friends"))
        self.events_tab.setText(_translate("MainWindow", "Events"))
        self.noti_tab.setText(_translate("MainWindow", "Notifications"))
        self.event_title.setText(_translate("MainWindow", "Events:"))
        self.log_out_button_2.setText(_translate("MainWindow", "Log Out"))
        item = self.eventTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Host"))
        item = self.eventTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.eventTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date/Time"))
        item = self.eventTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        self.addEventButton.setText(_translate("MainWindow", "Add Event"))
        self.dateTimeLabel.setText(_translate("MainWindow", "Date/Time: (mm/dd/yyyy, time)"))
        self.locationLabel.setText(_translate("MainWindow", "Location: "))
        self.descriptionLabel.setText(_translate("MainWindow", "Description:"))
        self.publishEventButton.setText(_translate("MainWindow", "Publish Event"))
        self.backToEventsButton.setText(_translate("MainWindow", "Back"))
        self.friends_tab_2.setText(_translate("MainWindow", "Friends"))
        self.noti_tab_2.setText(_translate("MainWindow", "Notifications"))
        self.events_tab_2.setText(_translate("MainWindow", "Events"))
        self.flist_title.setText(_translate("MainWindow", "Friends List"))
        self.suggested_friend_list_title.setText(_translate("MainWindow", "Suggested friends for you:"))
        self.log_out_button_3.setText(_translate("MainWindow", "Log Out"))
        self.uname_addfriend_label.setText(_translate("MainWindow", "Username: "))
        self.addfriend_button.setText(_translate("MainWindow", "Add friend"))
        self.add_friend_header.setText(_translate("MainWindow", "Enter Username Below to Add a Friend"))
        self.friends_tab_3.setText(_translate("MainWindow", "Friends"))
        self.noti_tab_3.setText(_translate("MainWindow", "Notifications"))
        self.events_tab_3.setText(_translate("MainWindow", "Events"))
        self.noti_title.setText(_translate("MainWindow", "Notifications:"))
        self.log_out_button.setText(_translate("MainWindow", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
