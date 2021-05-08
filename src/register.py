# register.py
# Shows Login dialog
# When "Daftar" is clicked checks registration details (opens new dialog box if registration fails), switches to login window when registration succeeds
# When "Login" is clicked, switches to login window

import string
import variables
import login

# database
from backend import getUserInfo, addUserInfo

# widget needs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        variables.widget.setFixedWidth(320)
        variables.widget.setFixedHeight(350)
        loadUi("ui/register.ui", self)
        self.registerButton.clicked.connect(self.userRegister)
        self.gotoLogin.clicked.connect(self.goLogin)
        self.username.setPlaceholderText('Username...')
        self.email.setPlaceholderText('Email...')
        self.password.setPlaceholderText('Kata sandi...')
        self.name.setPlaceholderText('Nama...')
        self.address.setPlaceholderText('Alamat...')
        self.phone.setPlaceholderText('Nomor telepon...')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def userRegister(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        name = self.name.text()
        address = self.address.text()
        phone = self.phone.text()
        
        if username == "" or email == "" or password == "" or name == "" or address == "" or phone == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Masukkan field yang diperlukan.")
            msg.setWindowTitle("Register failed.")
            msg.exec_()
        elif len(username) < 6:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username harus setidaknya 6 karakter.")
            msg.setWindowTitle("Register failed.")
            msg.exec_()
        elif "@" not in email or "." not in email or " " in email:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Email yang dimasukkan tidak valid.")
            msg.setWindowTitle("Register failed.")
            msg.exec_()
        elif len(password) < 6:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Password harus setidaknya 6 karakter.")
            msg.setWindowTitle("Register failed.")
            msg.exec_()
        elif not phone.isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Telepon yang dimasukkan tidak valid.")
            msg.setWindowTitle("Register failed.")
            msg.exec_()
        else:
            user1 = getUserInfo(username)
            user2 = getUserInfo(email)
            if user1 == None and user2 == None:
                addUserInfo(username, email, password, name, address, phone)
                self.goLogin()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Akun dengan username atau email yang digunakan sudah ada.")
                msg.setWindowTitle("Register failed.")
                msg.exec_()

            # print("Username:", username)
            # print("Email:", email)
            # print("Password:", password)
            # print("Nama:", name)
            # print("Alamat:", address)
            # print("No telepon:", phone)
        
    def goLogin(self):
        log = login.Login()
        variables.widget.addWidget(log)
        variables.widget.setCurrentIndex(variables.widget.currentIndex() + 1)