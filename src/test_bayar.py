import mysql.connector as mariadb

from backend import *
import pytest

username = 'planties'
password = '12345678'

connection = mariadb.connect(user=username,password=password,host='localhost',database='planties', port ='3306')

def test_CalculateTotalHarga():
    query = ''' SELECT cart.banyak_barang
        FROM cart, katalog WHERE cart.id_barang = katalog.id_barang and id_user = 1'''
    cursor = connection.cursor()
    cursor.execute(query)
    banyak_barang = cursor.fetchall()

    query = ''' SELECT katalog.harga
        FROM cart, katalog WHERE cart.id_barang = katalog.id_barang and id_user = 1'''
    cursor = connection.cursor()
    cursor.execute(query)
    harga_barang = cursor.fetchall()
    
    for data in calculateTotalHarga(1) :
        assert (data[0]*data[1] == banyak_barang*harga_barang)
