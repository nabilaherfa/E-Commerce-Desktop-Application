# login.py
# Shows Login dialog
# When "Masuk" is clicked checks login details (opens new dialog box if login fails), switches to main window when login succeeds
# When "Registrasi" is clicked, switches to registrasi window

import string
import variables

# goto's
import register
import window

# database
from backend import getUserInfo

# widget needs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/login.ui", self)
        variables.widget.setFixedWidth(320)
        variables.widget.setFixedHeight(230)
        self.loginButton.clicked.connect(self.userLogin)
        self.gotoRegister.clicked.connect(self.goRegister)
        self.userEmail.setPlaceholderText('Username atau email...')
        self.password.setPlaceholderText('Kata sandi...')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def userLogin(self):
        userEmail = self.userEmail.text()
        password = self.password.text()
        if userEmail == "" or password == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Masukkan field yang diperlukan.")
            msg.setWindowTitle("Login failed.")
            msg.exec_()
        else:
            user = getUserInfo(userEmail)
            # If user exists, log in
            if user != None:
                if user[3] == password:
                    variables.curIDUser = user[0]
                    variables.curUsername = user[1]
                    self.goMainWindow()
            # If user does not exist, display message
            if variables.curIDUser == -1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Username atau password yang dimasukkan salah.")
                msg.setWindowTitle("Login failed.")
                msg.exec_()

    def goRegister(self):
        reg = register.Register()
        variables.widget.addWidget(reg)
        variables.widget.setCurrentIndex(variables.widget.currentIndex() + 1)

    def goMainWindow(self):
        mw = window.MyWindow()
        variables.widget.addWidget(mw)
        variables.widget.setFixedHeight(750)
        variables.widget.setFixedWidth(1300)
        variables.widget.setCurrentIndex(variables.widget.currentIndex() + 1)