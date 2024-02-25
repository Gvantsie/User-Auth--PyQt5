import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.login_button.clicked.connect(self.login_function)
        self.pushButton_2.clicked.connect(self.goto_create)

    def login_function(self):
        username = self.user_name.text()
        password = self.password.text()

        correct_username = "Gvantsa"
        correct_password = "TBC"

        if username == correct_username and password == correct_password:
            self.show_successful_login_ui()
        else:
            self.message.setText("Login or password are incorrect")

    #@staticmethod
    def show_successful_login_ui(self):
        successful_login_ui = SuccessfulLoginUI()
        widget.addWidget(successful_login_ui)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def goto_create(self):
        create_acc = CreateAcc()
        widget.addWidget(create_acc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("newacc.ui", self)
        self.signup.clicked.connect(self.create_acc_function)

    def create_acc_function(self):
        if self.password.text() == self.confirmpass.text():
            self.message1.setText("Successfully created account")
        else:
            self.message1.setText("Passwords do not match")


class SuccessfulLoginUI(QDialog):
    def __init__(self):
        super(SuccessfulLoginUI, self).__init__()
        loadUi("successfullogin.ui", self)

app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(570)
widget.setFixedHeight(700)
widget.show()
app.exec_()
