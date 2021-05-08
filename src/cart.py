from PyQt5 import QtCore, QtGui, QtWidgets
from backend import *

class cart_area(object):
   def __init__(self,user_id):
        super().__init__()
        self.pushButton = QtWidgets.QPushButton("Simpan Perubahan atau Lakukan Pembayaran")
        self.data = getCartOf(user_id)
        self.spinBoxList = []

   def setupUi(self, ScrollArea):
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.resize(205, 248)
        
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 555, 362))
        self.scrollAreaWidgetContents.setStyleSheet("background-color:#FCF0CC;")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        for d in self.data:
                # product_widget
                self.product_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
                self.product_widget.setStyleSheet("QWidget{\n"
                "background-color:#495c52;border-radius:25px;opacity:50%;\n"
                "}\n"
                "")
                self.product_widget.setObjectName("product_widget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.product_widget)
                self.horizontalLayout.setContentsMargins(20, -1, 12, 20)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.image_label = QtWidgets.QLabel(self.product_widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(10)
                sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
                self.image_label.setSizePolicy(sizePolicy)
                self.image_label.setMinimumSize(QtCore.QSize(150, 100))
                self.image_label.setMaximumSize(QtCore.QSize(200, 200))
                self.image_label.setAutoFillBackground(False)
                self.image_label.setStyleSheet("")
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(d[3])
                self.image_label.setPixmap(pixmap)
                self.image_label.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.image_label.setLineWidth(2)
                self.image_label.setText("")
                self.image_label.setScaledContents(False)
                self.image_label.setWordWrap(False)
                self.image_label.setObjectName("image_label")
                self.horizontalLayout.addWidget(self.image_label)
                self.desc_label = QtWidgets.QLabel(self.product_widget)
                text = str(d[0]) +'\n\nStok tersisa  : ' + str(d[4]) + '\nHarga           : ' +str(d[2])
                self.desc_label.setText(text)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.desc_label.sizePolicy().hasHeightForWidth())
                self.desc_label.setSizePolicy(sizePolicy)
                self.desc_label.setMinimumSize(QtCore.QSize(349, 150))
                self.desc_label.setStyleSheet("font-size:16px;color:#FCF0CC;\n""")
                self.desc_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.desc_label.setObjectName("desc_label")
                self.horizontalLayout.addWidget(self.desc_label)
                spinBox = QtWidgets.QSpinBox()
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(spinBox.sizePolicy().hasHeightForWidth())
                spinBox.setSizePolicy(sizePolicy)
                spinBox.setMinimumSize(QtCore.QSize(55, 35))
                spinBox.setMaximumSize(QtCore.QSize(80, 45))
                spinBox.setSizeIncrement(QtCore.QSize(0, 0))
                font = QtGui.QFont()
                font.setFamily("Futura")
                spinBox.setFont(font)
                spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
                spinBox.setAutoFillBackground(False)
                spinBox.setStyleSheet("background-color:#bbdbb4;")
                spinBox.setAlignment(QtCore.Qt.AlignCenter)
                spinBox.setProperty("value", d[1]) # value adalah banyak_barang di cart
                spinBox.setMaximum(d[4])
                spinBox.setDisplayIntegerBase(10)
                spinBox.setObjectName("spinBox")
                self.horizontalLayout.addWidget(spinBox)
                self.spinBoxList.append(spinBox)
                self.verticalLayout.addWidget(self.product_widget)

        if (len(self.data) == 0):
                empty_cart_label = QtWidgets.QLabel("\nKeranjang kosong. Belanja dulu, yuk!")
                empty_cart_label.setStyleSheet(
                "color:#861657;\n"
                "font-size:20px;\n"
                "text-align:center;\n")
                self.verticalLayout.addWidget(empty_cart_label,alignment=QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        else:
                # add pushButton ke form pembayaran
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                self.pushButton.setSizePolicy(sizePolicy)
                self.pushButton.setMinimumSize(QtCore.QSize(450, 50))
                self.pushButton.setMaximumSize(QtCore.QSize(700, 50))
                self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton.setMouseTracking(True)
                self.pushButton.setStyleSheet("QPushButton{background-color:#861657;\n"
                "color:#FCF0CC;\n"
                "font-size:15px;\n"
                "text-align:center;\n"
                "padding:8% 3%;\n"
                "border-style: outset;\n"
                "border-radius:25px;}\n"
                "QPushButton:hover\n"
                "{\n"
                "   background-color:#A64253;\n"
                "}\n"
                "          ")
                self.pushButton.setObjectName("pushButton")
                self.verticalLayout.addWidget(self.pushButton,alignment=QtCore.Qt.AlignCenter)                

        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        QtCore.QMetaObject.connectSlotsByName(ScrollArea)

def updattingCart(spinBoxList,data):
        i = 0
        dataCounter = 0
        dataToUpdate = []
        for spinBox in spinBoxList:
                if (spinBox.value() == 0):#data akan didelete dr cart
                        deleteFromCart(data[i][5],data[i][6])
                elif (spinBox.value() != data[i][1]): #data akan diupdate
                        dataCounter+=1
                        dataToUpdate.append([data[i][5],data[i][6],spinBox.value()])
                i+=1
        updateCart(dataCounter,False,dataToUpdate)

def insertingCart(cart_data):
        print(cart_data)
        addToCart(len(cart_data),cart_data)

def updateKatalogStock(cart_data):
        for i in range (len(cart_data)):
                id_barang = cart_data[i][6]
                new_stok = cart_data[i][4] - cart_data[i][1]
                updateStok(id_barang,new_stok)

def cleanCart(cart_data):
        for i in range (len(cart_data)):
                deleteFromCart(cart_data[i][5],cart_data[i][6])
