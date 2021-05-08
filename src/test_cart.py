import mysql.connector as mariadb

from backend import *
from cart import cleanCart

username = 'planties'
password = '12345678'

connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')

def testBanyakDataPadaCart():
    query = ''' SELECT count(id_barang) FROM cart WHERE id_user = 1'''
    cursor = connection.cursor()
    cursor.execute(query)
    banyak_cart = cursor.fetchall()[0][0]
    assert (len(getCartOf(1)) == banyak_cart)

def getCurrentBanyakBarang():
    query = '''SELECT banyak_barang FROM cart WHERE id_user = 1 and id_barang = 2'''
    cursor = connection.cursor()

    cursor.execute(query)
    banyak_barang_lama = cursor.fetchall()
    print(banyak_barang_lama)
    return banyak_barang_lama

def testAddToCart():
    cart = getCartOf(1)
    addToCart(1,[[1,2,1]]) # urutan elemen array data : id_user, id_barang, banyak_barang(yg ingin ditambahkan)
    
    update = False
    for data in cart:
        if data[6] == 2:
            update = True
            banyak_barang_lama = data[1]

    cart = getCartOf(1)

    for data in cart:
            if data[6] == 2:
                banyak_barang_baru = data[1]

    stok_barang = getProduct(2)[0][3]

    if not update: # data seharusnya diinsert sehingga banyak barang menjadi 1
        assert banyak_barang_baru == 1
    else:
        if (banyak_barang_lama + 2 <= stok_barang):
            assert banyak_barang_baru == banyak_barang_lama + 2
        else:
            assert banyak_barang_baru == stok_barang

def testCleanCart():
    cart = getCartOf(1) #mendapatkan data cart user id = 1 yg lama
    cleanCart(cart) #menghapus cart user id = 1 
    cart = getCartOf(1) #mendapatkan data cart user id = 1 yg baru
    assert len(cart) == 0