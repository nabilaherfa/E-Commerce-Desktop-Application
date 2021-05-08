from PyQt5 import QtCore, QtGui, QtWidgets

from backend import calculateTotalHarga

class Ui_Bayar(object):
        def __init__(self,user_id):
                super().__init__()
                self.pushButton = QtWidgets.QPushButton("Bayar Sekarang")
                self.data = calculateTotalHarga(user_id)
                self.radioButton = ""
                self.radioButton_2 = ""
                self.radioButton_3 = ""

        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(1000, 618)
                self.verticalLayout = QtWidgets.QVBoxLayout(Form)
                self.verticalLayout.setObjectName("verticalLayout")
                
                total_harga = 0
                for a in self.data:
                        total_harga += a[0]*a[1]
                        
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setStyleSheet("background-color:rgb(252, 240, 204);\n"
                        "border-radius:30px;\n"
                        "border:10 px solid black;\n"
                        "")
                self.widget.setObjectName("widget")
                self.label = QtWidgets.QLabel(self.widget)
                self.label.setText("Metode Pembayaran")
                self.label.setGeometry(QtCore.QRect(38, 14, 311, 48))
                self.label.setStyleSheet("color:rgb(134, 22, 87);font: 28pt \"Times New Roman\";")
                self.label.setObjectName("label")
                self.radioButton = QtWidgets.QRadioButton(self.widget)
                self.radioButton.setGeometry(QtCore.QRect(43, 97, 21, 49))
                self.radioButton.setStyleSheet("color: rgb(255, 0, 0);")
                self.radioButton.setText("")
                self.radioButton.setObjectName("radioButton")
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setText("Transfer Manual")
                self.label_2.setGeometry(QtCore.QRect(100, 97, 231, 49))
                self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);color: rgb(134, 22, 87);font: 16pt \"Times New Roman\";border-radius:10px;\n"
                        "")
                self.label_2.setObjectName("label_2")
                self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
                self.radioButton_2.setGeometry(QtCore.QRect(43, 174, 16, 49))
                self.radioButton_2.setStyleSheet("color: rgb(255, 0, 0);")
                self.radioButton_2.setText("")
                self.radioButton_2.setObjectName("radioButton_2")
                self.label_3 = QtWidgets.QLabel(self.widget)
                self.label_3.setText("OVO")
                self.label_3.setGeometry(QtCore.QRect(100, 174, 231, 49))
                self.label_3.setStyleSheet("font: 75 16pt \"Times New Roman\";background-color: rgb(255, 255, 255);color:rgb(134, 22, 87);border-radius:10px;")
                self.label_3.setObjectName("label_3")
                self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
                self.radioButton_3.setGeometry(QtCore.QRect(43, 251, 21, 49))
                self.radioButton_3.setStyleSheet("color: rgb(255, 0, 0);")
                self.radioButton_3.setText("")
                self.radioButton_3.setObjectName("radioButton_3")
                self.label_4 = QtWidgets.QLabel(self.widget)
                self.label_4.setText("BCA Virtual Account")
                self.label_4.setGeometry(QtCore.QRect(100, 251, 231, 49))
                self.label_4.setStyleSheet("font: 16pt \"Times New Roman\";background-color: rgb(255, 255, 255);color: rgb(134, 22, 87);border-radius:10px")
                self.label_4.setMidLineWidth(-3)
                self.label_4.setTextFormat(QtCore.Qt.PlainText)
                self.label_4.setObjectName("label_4")
                self.pushButton= QtWidgets.QPushButton(self.widget)
                self.pushButton.setText("Bayar Sekarang")
                self.pushButton.setGeometry(QtCore.QRect(360, 370, 301, 44))
                self.pushButton.setStyleSheet('''
                        QPushButton{
                                background-color: rgb(166, 66, 83);
                                border-radius:10px;
                                font: 16pt \"Times New Roman\";
                                color: rgb(255, 255, 255);
                        }
                        QPushButton::hover{
                                background-color: #495c52;
                                color:#861657;
                        }
                ''')
                self.pushButton.setObjectName("pushButton")
                self.label_11 = QtWidgets.QLabel(self.widget)
                self.label_11.setGeometry(QtCore.QRect(740, 260, 191, 25))
                self.label_11.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.label_10 = QtWidgets.QLabel(self.widget)
                self.label_10.setGeometry(QtCore.QRect(670, 190, 191, 25))
                self.label_10.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_10.setText("")
                self.label_10.setObjectName("label_10")
                self.widget_2 = QtWidgets.QWidget(self.widget)
                self.widget_2.setGeometry(QtCore.QRect(350, 60, 321, 301))
                self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.widget_2.setObjectName("widget_2")
                self.label_6 = QtWidgets.QLabel(self.widget_2)
                self.label_6.setText("Ringkasan Pembayaran")
                self.label_6.setGeometry(QtCore.QRect(70, 20, 201, 32))
                self.label_6.setStyleSheet("font: 16pt \"Times New Roman\";\n"
                        "")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.widget_2)
                self.label_7.setText("Total Transaksi            " + "Rp." + str(total_harga))
                self.label_7.setGeometry(QtCore.QRect(40, 94, 251, 24))
                self.label_7.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.widget_2)
                self.label_8.setText("Biaya Pelayanan")
                self.label_8.setGeometry(QtCore.QRect(40, 147, 121, 24))
                self.label_8.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.widget_2)
                self.label_9.setText("Total Tagihan : " + "Rp." + str(5000+(total_harga)))
                self.label_9.setGeometry(QtCore.QRect(40, 241, 251, 24))
                self.label_9.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_9.setObjectName("label_9")
                self.line = QtWidgets.QFrame(self.widget_2)
                self.line.setGeometry(QtCore.QRect(20, 210, 311, 4))
                self.line.setStyleSheet("color: rgb(161, 161, 161);\n"
                        "background-color: rgb(140, 140, 140);")
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.label_13 = QtWidgets.QLabel(self.widget_2)
                self.label_13.setGeometry(QtCore.QRect(190, 147, 111, 24))
                self.label_13.setStyleSheet("font: 14pt \"Times New Roman\";")
                self.label_13.setText("")
                self.label_13.setObjectName("label_13")
                self.label_15 = QtWidgets.QLabel(self.widget_2)
                self.label_15.setText("Rp. 5.000")
                self.label_15.setGeometry(QtCore.QRect(220, 150, 71, 20))
                self.label_15.setStyleSheet("font: 12pt \"Times New Roman\";")
                self.label_15.setObjectName("label_15")
                self.verticalLayout.addWidget(self.widget)         
                QtCore.QMetaObject.connectSlotsByName(Form)