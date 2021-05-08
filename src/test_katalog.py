import mysql.connector as mariadb

from backend import *
from katalog import *

username = 'planties'
password = '12345678'

connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')

def testBanyakDataYangDitampilakan():
    query = ''' SELECT count(id_barang) FROM katalog'''
    cursor = connection.cursor()
    cursor.execute(query)
    banyak_katalog = cursor.fetchall()[0][0]
    assert (len(getDataForKatalog()) == banyak_katalog)

def testSearch():
    query = '''SELECT count(id_barang) FROM katalog,toko WHERE katalog.id_toko = toko.id_toko and nama_barang LIKE '%tanaman%hias%' or nama_toko like '%tanaman%hias%' '''
    cursor = connection.cursor()
    cursor.execute(query)
    banyak_katalog = cursor.fetchall()[0][0]
    assert (len(search("tanaman hias")) == banyak_katalog)