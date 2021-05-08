# main.py
# Opens "Login" when first clicked, login page will add other pages to variables.widget during runtime

import sys
import string
import variables

# goto's
import login

# database
from backend import database

# widget needs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow

firstwindow = login.Login()
variables.widget.addWidget(firstwindow)

variables.widget.show()
variables.app.exec_()