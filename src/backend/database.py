import mysql.connector as mariadb

username = 'planties'
password = '12345678'

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def getUserData(id_user):
    print("Load profile picture...")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = """SELECT id_user, nama, username,foto FROM user WHERE id_user = %s"""
        tuple = (str(id_user),)
        cursor.execute(query,tuple)
        result = cursor.fetchall()
        print("Data loaded successfully ")
    except mariadb.Error as error:
        print("Failed load user data {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        return result

def addKatalog(id_barang, id_toko, nama_barang, panjang, lebar, tinggi, berat,  harga, stok, filepath , deskripsi):
    print("Inserting data into katalog table")
    global username, password
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        foto = convertToBinaryData(filepath)
        query = """ INSERT INTO katalog
                          (id_barang, id_toko, nama_barang, panjang, lebar, tinggi, berat,  harga, stok, foto, deskripsi)
                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        # Convert data into tuple format
        insert_tuple = (id_barang, id_toko, nama_barang, panjang, lebar, tinggi, berat,  harga, stok, foto, deskripsi)
        cursor.execute(query, insert_tuple)
        connection.commit()
        print("Image and file inserted successfully ")
    except mariadb.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getDataForKatalog():
    print("Getting data from katalog table")
    global username, password
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = ''' SELECT nama_barang, nama_toko, stok, harga, foto, id_barang 
        FROM katalog, toko WHERE katalog.id_toko = toko.id_toko'''

        cursor.execute(query)
        katalog = cursor.fetchall()

        print("data fetched successfully ")
        return katalog
    except mariadb.Error as error:
        print("Failed getting data from katalog table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def addToCart(n,newdata):
    print("Inserting data into cart table ... ")
    try:

        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        
        for i in range (n):
            execute = False
            id_user = newdata[i][0]
            id_barang = newdata[i][1]
            banyak_barang = newdata[i][2]

            cursor.execute("select stok from katalog where id_barang = %s",(str(id_barang),))
            stok = cursor.fetchall()[0][0]

            query = '''SELECT banyak_barang FROM cart WHERE id_user = %s and id_barang = %s'''
            data_tuple = (str(id_user),str(id_barang))
            cursor.execute(query,data_tuple)
            data = cursor.fetchall()

            if (len(data) == 0):
                if (banyak_barang <= stok):
                    print("111")
                    execute = True
                    query = '''INSERT INTO cart (id_user,id_barang,banyak_barang) values (%s,%s,%s)'''
                    data_tuple = (str(id_user),str(id_barang),str(banyak_barang))
            else:
                if (banyak_barang + data[0][0] <= stok):
                    print("222")
                    execute = True
                    query = '''UPDATE cart SET banyak_barang = %s WHERE id_user = %s and id_barang = %s'''
                    data_tuple = (str(data[0][0] + banyak_barang),str(id_user),str(id_barang))

            if (execute):
                cursor.execute(query,data_tuple)
                connection.commit()
        print("data inserted successfully")
    except mariadb.Error as error:
        print("Failed inserting data to cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getProduct(id):
    print("Getting a product from katalog table")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = '''SELECT id_barang, nama_barang, nama_toko, stok, panjang, lebar, tinggi, berat, harga, foto,
        deskripsi, alamat_toko FROM katalog, toko WHERE katalog.id_toko = toko.id_toko and katalog.id_barang = %s'''
        tuple = (str(id),)
        cursor.execute(query,tuple)
        product = cursor.fetchall()

        print("data fetched successfully")
        return product
    except mariadb.Error as error:
        print("Failed getting data from katalog table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def updateCart(n,insert,data):
    print("Updatting data into cart table ... ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()

        for i in range (n):
            id_user = data[i][0]
            id_barang = data[i][1]
            banyak_barang = data[i][2]

            if (insert):
                query = '''INSERT INTO cart (id_user,id_barang,banyak_barang) values (%s,%s,%s)'''
                data_tuple = (str(id_user),str(id_barang),str(banyak_barang))
            else:
                query = '''UPDATE cart SET banyak_barang = %s WHERE id_user = %s and id_barang = %s'''
                data_tuple = (str(banyak_barang),str(id_user),str(id_barang))

            cursor.execute(query,data_tuple)
            connection.commit()
        print("data inserted successfully")
    except mariadb.Error as error:
        print("Failed inserting data to cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getCartOf(id_user):
    print("Getting cart..")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = "SELECT nama_barang, banyak_barang, harga, foto, stok, cart.id_user,cart.id_barang,katalog.id_toko FROM cart, katalog WHERE cart.id_barang = katalog.id_barang and cart.id_user = %s"

        tuple = (str(id_user),)
        cursor.execute(query,tuple)
        cart = cursor.fetchall()
        print("data fetched successfully")
        return cart
    except mariadb.Error as error:
        print("Failed getting data from cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def deleteFromCart(id_user,id_barang):
    print("Deleting data from cart table ... ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = '''DELETE FROM cart WHERE id_user = %s and id_barang = %s'''
        data_tuple = (str(id_user),str(id_barang))
        cursor.execute(query,data_tuple)
        connection.commit()
        print("data deleted successfully")
    except mariadb.Error as error:
        print("Failed deleting data from cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def addUserInfo(user, email, pw, name, address, phone):
    print("Inserting data into user table")
    global username, password
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = "SELECT count(id_user) from user"
        cursor.execute(query)
        count = cursor.fetchone()

        userid = count[0] + 1
        foto = convertToBinaryData("../img/profile.png")
        query = "INSERT INTO user (id_user, username, email, password, nama, alamat, no_telepon, foto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        # Convert data into tuple format
        insert_tuple = (userid, user, email, pw, name, address, phone, foto)
        result = cursor.execute(query, insert_tuple)
        connection.commit()
        print("Image and file inserted successfully ", result)
    except mariadb.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def setMetodePembayaran(id_transaksi, id_toko, id_pembeli, id_pesanan,status, nama_metode) :
    print("Setting metode_pembayaran ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        
        query = """ INSERT INTO transaksi
                          (id_transaksi, id_toko, id_pembeli, id_pesanan,status,metode_pembayaran)
                          VALUES (%s,%s,%s,%s,%s,%s)"""
                          
        insert_tuple = (id_transaksi, id_toko, id_pembeli, id_pesanan,status, nama_metode)
        result = cursor.execute(query, insert_tuple)
        connection.commit()
        print("File inserted successfully ", result)
    except mariadb.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getRatingOf(id_barang):
    print("Getting rating..")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = '''SELECT user.nama, rating, testimoni
        FROM rating, user WHERE rating.id_pengguna = user.id_user and rating.id_barang = %s'''

        tuple = (str(id_barang),)
        cursor.execute(query,tuple)
        data = cursor.fetchall()
        print("data fetched successfully")
        return data
    except mariadb.Error as error:
        print("Failed getting data from rating table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def addPesanan(id_user, id_barang, banyak_barang) :
    print("add pesanan ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()

        cursor.execute("select id_pesanan from pesanan")
        id_pesanan = len(cursor.fetchall()) + 1
        print("id pesanan : ", id_pesanan)

        query = """ INSERT INTO pesanan
                          (id_pesanan, id_user, id_barang, banyak_barang)
                          VALUES (%s,%s,%s,%s)"""
                          
        insert_tuple = (id_pesanan,id_user, id_barang, banyak_barang)
        cursor.execute(query, insert_tuple)
        connection.commit()
        print("File inserted successfully ")
        return id_pesanan
    except mariadb.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getAvgRatingOf(id_barang):
    print("Getting rating..")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = '''SELECT avg(rating)
        FROM rating WHERE rating.id_barang = %s'''

        tuple = (str(id_barang),)
        cursor.execute(query,tuple)
        avg_rating = cursor.fetchall()
        print("data fetched successfully")
        if (avg_rating[0][0] == None):
            return "-"
        return avg_rating[0][0]
    except mariadb.Error as error:
        print("Failed getting data from rating table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def calculateTotalHarga(id_user) :
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = ''' SELECT cart.banyak_barang,  katalog.harga
        FROM cart, katalog WHERE cart.id_barang = katalog.id_barang and cart.id_user = %s'''

        data_tuple = (str(id_user),)
        cursor.execute(query,data_tuple)
        data = cursor.fetchall()
        
        print("File inserted successfully ")
        
        return data
    
    except mariadb.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def updateStok(id_barang,new_stock):
    print("Updatting stock data into catalog table ... ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()

        query = '''UPDATE katalog SET stok = %s WHERE id_barang = %s'''
        data_tuple = (str(new_stock),str(id_barang))
        cursor.execute(query,data_tuple)
        connection.commit()
        query = '''DELETE FROM katalog WHERE stok = 0'''
        cursor.execute(query)
        connection.commit()
        print("data inserted successfully")
    except mariadb.Error as error:
        print("Failed inserting data to cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getTransaksi(id_user):
    print("Get transaksi of..")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = '''SELECT transaksi.id_transaksi, toko.nama_toko, user.nama, pesanan.id_pesanan, transaksi.status, transaksi.metode_pembayaran, katalog.nama_barang, katalog.foto, pesanan.id_barang FROM transaksi, pesanan, katalog, toko, user 
        WHERE transaksi.id_pesanan = pesanan.id_pesanan and pesanan.id_barang = katalog.id_barang and katalog.id_toko = toko.id_toko and transaksi.id_pembeli = user.id_user and transaksi.id_pembeli = %s'''

        tuple = (str(id_user),)
        cursor.execute(query,tuple)
        cart = cursor.fetchall()
        print("data fetched successfully")
        return cart
    except mariadb.Error as error:
        print("Failed getting data from cart table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getKatalogByKeyword(input_search):
    print("Getting data from katalog table")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = ''' SELECT nama_barang, nama_toko, stok, harga, foto, id_barang 
        FROM katalog, toko WHERE katalog.id_toko = toko.id_toko and (nama_barang like %s or nama_toko like %s)'''
        tuple = (input_search,input_search)
        cursor.execute(query,tuple)
        katalog = cursor.fetchall()

        print("data fetched successfully ")
        return katalog
    except mariadb.Error as error:
        print("Failed getting data from katalog table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getPesanan(id_user):
    print("Getting pesanan..")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = "SELECT id_pesanan, id_user, id_barang, banyak_barang FROM pesanan WHERE id_user = %s"

        tuple = (str(id_user),)
        cursor.execute(query,tuple)
        pesanan = cursor.fetchall()
        print("data fetched successfully")
        return pesanan
    except mariadb.Error as error:
        print("Failed getting data from pesanan table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getUserInfo(userEmail):
    print("Getting user info from user table")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        query = ''' SELECT * FROM user WHERE username = %s or email = %s'''

        cursor.execute(query, (userEmail, userEmail))
        user = cursor.fetchone()

        print("data fetched successfully")
    except mariadb.Error as error:
        print("Failed getting data from user table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return user

            
def addTransaksi(id_toko, id_pembeli, id_pesanan, status, metode_pembayaran) :
    print("add transaksi ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()
        
        cursor.execute("select id_transaksi from transaksi")
        id_transaksi = len(cursor.fetchall()) + 1
        print(id_transaksi)

        query = """ INSERT INTO transaksi
                          (id_transaksi, id_toko, id_pembeli, id_pesanan, status ,metode_pembayaran)
                          VALUES (%s,%s,%s,%s,%s,%s)"""
                          
        insert_tuple = (id_transaksi, id_toko, id_pembeli, id_pesanan, status,metode_pembayaran)
        cursor.execute(query, insert_tuple)
        connection.commit()
        print("File inserted successfully ")
    except mariadb.Error as error:
                print("Failed getting data from transaksi table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def addRating(id_user,id_barang,rating,testimoni):
    print("add rating . . . ")
    try:
        connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')
        cursor = connection.cursor()

        query = """ INSERT INTO rating
                          (id_pengguna, id_barang, rating, testimoni)
                          VALUES (%s,%s,%s,%s)"""
                          
        insert_tuple = (id_user, id_barang, rating, testimoni)
        cursor.execute(query, insert_tuple)
        connection.commit()
        print("File inserted successfully ")
    except mariadb.Error as error:
                print("Failed getting data from transaksi table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()