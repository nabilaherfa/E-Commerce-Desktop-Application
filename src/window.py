# from PyQt5.Gui import QPixmap
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import * 

import sys
import variables,login
from backend import *
from cart import *
from detail_produk import *
from katalog import *
from cart import *
from bayar import *
from rating import *
from transaksi import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Planties')
        self.setWindowIcon(QIcon('Planties.png'))

        # set the size of window
        self.Width = 1000
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets

        self.header = QLabel("Planties")
        self.header.setStyleSheet('''color:#861657;font-size:50px;''')

        # ava
        self.profile_pict = QLabel(self)
        self.profile_pict.setObjectName('profile_pict')
        pixmap = QPixmap('../img/profile.png')
        pixmap.scaledToWidth(32)
        self.profile_pict.setPixmap(pixmap)

        #button
        self.btn_1 = QPushButton('Keranjang', self)
        self.btn_2 = QPushButton('Inbox', self)
        self.btn_3 = QPushButton('Transaksi', self)
        self.btn_4 = QPushButton('Logout', self)
        self.btn_t1 = QPushButton('Beranda', self)
        self.btn_t2 = QPushButton('Marketplace', self)
        self.btn_t3 = QPushButton('Forum', self)
        self.btn_t4 = QPushButton('Buku Panduan', self)
        self.btnbayar = QPushButton('Lanjutkan pembayaran', self)
        self.btnsold = QPushButton('Beli')

        self.btn_1.setObjectName('left_button')
        self.btn_2.setObjectName('left_button')
        self.btn_3.setObjectName('left_button')
        self.btn_4.setObjectName('left_button')
        self.btn_t1.setObjectName('top_button')
        self.btn_t2.setObjectName('top_button')
        self.btn_t3.setObjectName('top_button')
        self.btn_t4.setObjectName('top_button')

        self.btn_1.clicked.connect(self.button1)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_t1.clicked.connect(self.buttont1)
        self.btn_t2.clicked.connect(self.buttont2)
        self.btnbayar.clicked.connect(self.button3)

        self.btn_products = []
        self.btn_addToCart = QPushButton('', self)
        self.kalatalog_search_line = QLineEdit()
        
        self.btn_bayar = QPushButton('', self)
        self.btn_bayar.clicked.connect(self.button_bayar)
        self.btn_rating = QPushButton('', self)
        self.btn_rating.clicked.connect(self.button_rating)
        self.btnsold.clicked.connect(self.buttonsold)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5(-1)
        self.tab6 = self.ui6()
        self.tab7 = self.ui7(-1)

        # add cart
        self.cart = cart_area(variables.curIDUser)

        self.initUI()

    def initUI(self):
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.btn_t1)
        top_layout.addWidget(self.btn_t2)
        top_layout.addWidget(self.btn_t3)
        top_layout.addWidget(self.btn_t4)
        top_widget = QWidget()
        top_widget.setLayout(top_layout)
        top_widget.setStyleSheet('''
            QPushButton{
                background-color:#6C809A;
                color:#FCF0CC;
                font-size:14px;
                font-weight:400;
                text-align:center;
                padding:8% 3%;
                border-style: outset;
                border-radius:5px;
            }
            QPushButton#top_button:hover{
                background-color: #FCF0CC;
                color:#861657;
                font-weight:600;
            }
        ''')


        left_layout = QVBoxLayout()
        left_layout.addWidget(self.profile_pict)
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setStyleSheet('''
            QWidget{
                background-color:#495c52;
                margin:0;
                padding:0;
                border-radius:10px;
                padding:50px 0 0 0;
            }
            QPushButton{
                background-color:#6C809A;
                color:#FCF0CC;
                font-size:15px;
                font-weight:400;
                text-align:center;
                padding:8% 3%;
                border-style: outset;
                border-radius:5px;
            }
            QPushButton#left_button:hover{
                background-color: #FCF0CC;
                color:#861657;
                font-weight:600;
            }
        ''')


        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '') #DETAIL PRODUK : ID 4
        self.right_widget.addTab(self.tab6, '') #FORM BAYAR : ID 5
        self.right_widget.addTab(self.tab7, '') #FORM RATING : ID 6

        self.right_widget.setCurrentIndex(1)
        self.right_widget.setStyleSheet('''
        QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}
        ''')
        self.contentWidth = self.right_widget.sizeHint().width()
        
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.header)
        right_layout.addWidget(top_widget)
        right_layout.addWidget(self.right_widget)
        right_content = QWidget()
        right_content.setLayout(right_layout)
        

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_content)
        main_layout.setStretch(0, 35)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        main_widget.setStyleSheet('''
            background-color:#BBDBB4;
        ''')
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)
        self.clean()
        self.btn_1.setStyleSheet('''font-weight:600;background-color: #FCF0CC;color:#861657;''')

    def button2(self):
        self.right_widget.setCurrentIndex(1)
        self.clean()
        self.btn_2.setStyleSheet('''font-weight:600;background-color: #FCF0CC;color:#861657;''')

    def button3(self):
        self.right_widget.setCurrentIndex(2)
        self.clean()
        self.btn_3.setStyleSheet('''font-weight:600;background-color: #FCF0CC;color:#861657;''')

    def button4(self):
        variables.curIDUser = -1
        variables.curUsername = "null"
        log = login.Login()
        variables.widget.addWidget(log)
        variables.widget.setCurrentIndex(variables.widget.currentIndex() + 1)
    
    def buttont1(self):
        self.right_widget.setCurrentIndex(1)
        self.clean()
        self.btn_t1.setStyleSheet('''font-weight:600;background-color: #FCF0CC;color:#861657;''')
    
    def buttont2(self):
        self.right_widget.setCurrentIndex(1)
        self.clean()
        self.btn_t2.setStyleSheet('''font-weight:600;background-color: #FCF0CC;color:#861657;''')

    def button_product(self,id_product):
        self.right_widget.removeTab(4)
        self.right_widget.insertTab(4,self.ui5(id_product),'')
        # self.tab_product = self.ui5(id_product)
        # id = self.right_widget.addTab(self.tab_product, '')
        self.right_widget.setCurrentIndex(4)
        self.clean()
    
    def button_search(self):
        # update tab widget for katalog page
        self.right_widget.removeTab(1)
        self.right_widget.insertTab(1,self.ui2(),'')
        self.right_widget.setCurrentIndex(1)

    def connectButtonProduct(self):
        i = 0
        for id in self.list_idproducts:
            self.btn_products[i].clicked.connect(lambda state, x=id: self.button_product(x))
            i+=1
    
    def button_bayar(self) :
        #update cart
        updattingCart(self.spinBoxList,self.cartdata)

        #update form bayar
        self.right_widget.removeTab(5)
        self.right_widget.insertTab(5,self.ui6(),'')
        #update form keranjang
        self.right_widget.removeTab(0)
        self.right_widget.insertTab(0,self.ui1(),'')

        self.right_widget.setCurrentIndex(5)
        self.clean()
        
    def addDataRating(self,id_produk):
        selected_rating = self.ratingBox.currentText()
        review = self.testimoniBox.text()
        addRating(datarating[8], variables.curIDUser,selected_rating, review)

    def button_rating(self,id_produk) :
        self.right_widget.removeTab(6)
        self.right_widget.insertTab(6,self.ui7(id_produk),'')
        self.right_widget.setCurrentIndex(6)
        self.clean()

    def button_addToCart(self,data):
        insertingCart(data)
        self.right_widget.removeTab(0)
        self.right_widget.insertTab(0,self.ui1(),'')

    def buttonsold(self):
        # add data transaksi dan pesanan
        if (self.buttonoptmetodebayar1.isChecked()):
            metodebayar = "Transfer Manual"
        elif (self.buttonoptmetodebayar2.isChecked()):
            metodebayar = "OVO"
        else:
            metodebayar = "BCA Virtual Account"

        i = 0
        self.cartdata = getCartOf(variables.curIDUser)
        for data in self.cartdata:
            id_pesanan = addPesanan(variables.curIDUser,data[6],data[1])
            addTransaksi(data[7],variables.curIDUser,id_pesanan,"selesai",metodebayar)
            i+=1
        
        # update stock di katalog
        updateKatalogStock(self.cartdata)

        # clean cart
        cleanCart(self.cartdata)

        # update tab widget for katalog page
        self.right_widget.removeTab(1)
        self.right_widget.insertTab(1,self.ui2(),'')

        # update tab widget for cart page
        self.right_widget.removeTab(0)
        self.right_widget.insertTab(0,self.ui1(),'')

        # update tab widget for riwayat transaksi
        self.right_widget.removeTab(2)
        self.right_widget.insertTab(2,self.ui3(),'')

        self.right_widget.setCurrentIndex(2)
    # ----------------- 
    # functions

    def clean(self):
        self.btn_1.setStyleSheet('''''')
        self.btn_2.setStyleSheet('''''')
        self.btn_3.setStyleSheet('''''')
        self.btn_4.setStyleSheet('''''')
        self.btn_t1.setStyleSheet('''''')
        self.btn_t2.setStyleSheet('''''')
        self.btn_t3.setStyleSheet('''''')
        self.btn_t4.setStyleSheet('''''')

    # ----------------- 
    # pages

    def ui1(self):
        ScrollArea = QtWidgets.QScrollArea()
        cart = cart_area(variables.curIDUser)
        cart.setupUi(ScrollArea)

        self.cartdata = cart.data
        self.spinBoxList = cart.spinBoxList

        self.btnbayar = cart.pushButton
        self.btnbayar.clicked.connect(self.button_bayar)

        return ScrollArea

    def ui2(self):            
        ScrollArea = QtWidgets.QScrollArea()
        print(self.kalatalog_search_line.text())
        katalog = katalog_area(self.kalatalog_search_line.text())
        katalog.setupUi(ScrollArea)
        self.btn_products = katalog.btn_products
        self.list_idproducts = katalog.list_idProducts
        self.btn_search = katalog.btn_search
        self.kalatalog_search_line = katalog.line_edit
        self.btn_search.clicked.connect(self.button_search)
        self.connectButtonProduct()

        return ScrollArea
        
    def ui3(self):
        ScrollArea = QtWidgets.QScrollArea()
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.resize(205, 248)
        formT = QWidget()
        transaksi = Ui_Transaksi(variables.curIDUser)
        transaksi.setupUi(formT)
        
        self.btnratinglist = transaksi.ratingbuttonlist
        self.idbarangriwayatpesanan = transaksi.idbarang
        for i in range (len(self.idbarangriwayatpesanan)):
            self.btnratinglist[i].clicked.connect(lambda state, x=self.idbarangriwayatpesanan[i]:self.button_rating(x))
        ScrollArea.setWidget(formT)
        return ScrollArea
    
    def ui4(self):
        
        main_layout = QVBoxLayout()
        main = QWidget()

        main.setLayout(main_layout)
        return main
            
    def ui5(self,id_produk):
        ScrollArea = QtWidgets.QScrollArea()
        pageDetailProduct = DetailProduk(id_produk)
        pageDetailProduct.setupUi(ScrollArea)
        self.btn_addToCart = pageDetailProduct.pushButton_2
        print(id_produk)
        self.btn_addToCart.clicked.connect(lambda state, x=[[variables.curIDUser, id_produk, 1]]:self.button_addToCart(x))
        return ScrollArea
    
    def ui6(self):
        formB = QWidget()
        bayar = Ui_Bayar(variables.curIDUser)
        bayar.setupUi(formB)
        
        self.btnsold = bayar.pushButton
        self.btnsold.clicked.connect(self.buttonsold)
        self.buttonoptmetodebayar1 = bayar.radioButton
        self.buttonoptmetodebayar2 = bayar.radioButton_2
        self.buttonoptmetodebayar3 = bayar.radioButton_3

        return formB
    
    def ui7(self,id_produk):
        formR = QWidget()
        rating = Ui_Rating(id_produk)
        rating.setupUi(formR)
        
        self.ratingBox = rating.comboBox
        self.testimoniBox = rating.lineEdit

        self.btnRatingSubmition = rating.pushButton
        self.btnRatingSubmition.clicked.connect(lambda state, x = id_produk: self.rating_submitted(x))
        return formR

    def rating_submitted(self,id_produk):
        selected_rating = self.ratingBox.currentText()
        review = self.testimoniBox.text()
        print(selected_rating)
        print(review)
        addRating(variables.curIDUser,id_produk,selected_rating, review)
        #update katalog page
        self.right_widget.removeTab(1)
        self.right_widget.insertTab(1,self.ui2(),'')
        self.buttont1()

    def clickme(self):
        # printing pressed
        print("Pembayaran berhasil disimpan")

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())