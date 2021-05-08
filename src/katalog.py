from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from backend import *

# kelas untuk kolom search
class Ui_SearchWidget(object):
    def __init__(self):
        self.pushButton = QPushButton("")
        self.lineEdit = QLineEdit("")

    def setupUi(self, SearchWidget):
        SearchWidget.setObjectName("SearchWidget")
        SearchWidget.resize(755, 100)
        SearchWidget.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_2 = QVBoxLayout(SearchWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vboxlayout.setContentsMargins(-1, 0, -1, -1)
        self.vboxlayout.setObjectName("vboxlayout")
        self.widget = QWidget(SearchWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet("border-radius:5px;color:#a64253;padding-left:10px;background-color:white;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QPushButton(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(120, 35))
        self.pushButton.setMaximumSize(QSize(200, 35))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet('''
        QPushButton{border-radius:10px;background-color:#a64253;color:#fcf0cc;}
        QPushButton:hover{background-color:#6c809a;}''')
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.vboxlayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.vboxlayout)

        self.retranslateUi(SearchWidget)
        QMetaObject.connectSlotsByName(SearchWidget)

    def retranslateUi(self, SearchWidget):
        _translate = QCoreApplication.translate
        SearchWidget.setWindowTitle(_translate("SearchWidget", "Form"))
        self.pushButton.setText(_translate("SearchWidget", "Search"))

# kelas untuk halaman katalog
class katalog_area(object):
   def __init__(self,katalog_search_keyword):
        super().__init__()
        self.btn_products = []
        self.list_idProducts = []
        if (katalog_search_keyword == ""):
            self.katalog = getDataForKatalog() #tampilan katalog default
        else:
            self.katalog = search(katalog_search_keyword) #tampilan disesuaikan dengan keyword
        self.btn_search = QPushButton()
        self.line_edit = QLineEdit("")

   def setupUi(self, ScrollArea):
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.resize(205, 248)

        # header label
        header = QLabel("Penawaran Hari Ini")
        header.setStyleSheet('''color:#861657;font-size:30px;margin-top:15px;
                    margin-left:15px;''')

        # setup search widget
        SearchWidget = QWidget()
        search_ui = Ui_SearchWidget()
        search_ui.setupUi(SearchWidget)
        self.btn_search = search_ui.pushButton
        self.line_edit = search_ui.lineEdit
        
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 362))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.main_layout = QGridLayout(self.scrollAreaWidgetContents)
        self.main_layout.setObjectName("verticalLayout")

    
        col_counter = 0
        row_counter = 0
        counter = 0
        for i in self.katalog:
            label = QLabel()
            pixmap = QPixmap()
            pixmap.loadFromData(i[4])
            label.setPixmap(pixmap)
            # label.setStyleSheet('''
            # QLabel{width:10px;}''')
            # label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
            
            product_layout = QVBoxLayout()
            self.btn_products.append(QPushButton(i[0]))
            self.btn_products[counter].setStyleSheet('''
            QPushButton{
                font-size : 13px;
                font-weight : bold;
                border : none;
            }
            QPushButton::hover{
                color : #a64253;
            }
            ''')
            self.btn_products[counter].setCursor(QCursor(Qt.PointingHandCursor))
            self.list_idProducts.append(i[5])
            counter+=1

            product_layout.addWidget(self.btn_products[counter-1]) # nama barang
            product_layout.addWidget(label)
            product_layout.addWidget(QLabel('Toko : '+i[1]))  # nama toko
            product_layout.addWidget(QLabel('Rp'+str(i[3]))) # harga
            product_layout.addWidget(QLabel('Stok tersisa : '+str(i[2]))) # harga
            product_widget = QWidget()
            product_widget.setMaximumSize(QSize(350, 400))
            product_widget.setMinimumSize(QSize(200, 300))
            product_widget.setLayout(product_layout)
            product_widget.setStyleSheet('''background-color:#495c52;color:white;border-radius: 12px;
            QLabel{font-size:0.5vw;}
            QPixmap{width:5vw;}
            ''')
            product_widget.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)
            
            self.main_layout.addWidget(product_widget,row_counter,col_counter)
            col_counter+=1
            if (col_counter > 2):
                col_counter = 0
                row_counter+=1
    

        self.main_layout.setHorizontalSpacing(10)
        self.main_layout.setVerticalSpacing(15)

        self.scrollAreaWidgetContents.setLayout(self.main_layout)
        self.verticalcontent = QVBoxLayout()
        self.verticalcontent.addWidget(header)
        self.verticalcontent.addWidget(SearchWidget)
        self.verticalcontent.addWidget(self.scrollAreaWidgetContents)
        # self.verticalcontent.setSpacing(20)
        self.verticalwidget = QWidget()
        self.verticalwidget.setLayout(self.verticalcontent)

        ScrollArea.setWidget(self.verticalwidget)

        QMetaObject.connectSlotsByName(ScrollArea)

   def button_product(self,id_product):
        self.tab_product = self.ui5(id_product)
        id = self.right_widget.addTab(self.tab_product, '')
        self.right_widget.setCurrentIndex(id)
        self.clean()


def search(text_search):
    #olah text_search dari user
    text_search = text_search.split(" ")
    searchdlmlist = "%"
    for i in text_search:
        searchdlmlist += i + "%"

    dataHasilSearch = getKatalogByKeyword(searchdlmlist)
    return dataHasilSearch
