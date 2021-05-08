import mysql.connector as mariadb

from backend import *
from rating import *

username = 'planties'
password = '12345678'

connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')


def test_AddRating():
    addRating(2,3,5,"bagus banget, puas ama kualitas barang")

    query = ''' SELECT rating FROM rating WHERE id_barang = 3 AND id_pengguna = 2'''
    cursor = connection.cursor()
    cursor.execute(query)
    banyak = len(cursor.fetchall())
    assert banyak == 1
