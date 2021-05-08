# variables.py
# Global variables: widget for QStackWidget, curIDUser and curUsername for current user details (user_id, username)

import sys
from PyQt5 import QtWidgets

curIDUser = -1
curUsername = "null"

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()