Planties
> Here goes your awesome project description!

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Module](#module)
* [Implementasi Basis Data](#data)

## General info
Planties adalah desktop application untuk jual-beli tanaman yang diprogram dengan Python, didesain dengan Qt, dan memanfaatkan MySQL sebagai database system. Perangkat lunak ini memiliki fitur login, registrasi, menampilkan dan mencari katalog produk, melihat detail suatu produk dan testimoni/rating, penambahan barang yang akan dibeli ke keranjang, menampilkan form pembayaran, melihat riwayat transaksi, serta menambah rating.


## Technologies
* Python - version 3.9.1
* MariaDB - version 15.1

## Setup
Libraries
* Download repository.
* Pastikan library MySQL dan PyQt 5 sudah di-install, jika belum:
`pip install mysql-connector-python`
`pip install PyQt5`

Database configuration
* Jalankan MariaDB.
* Import planties.sql sebagai database lokal bernama 'planties'.
* Berikan privilege akses ke 'planties' dengan password '12345678', atau ubah variabel global `username` dan `password` pada database.py sesuai username dan password MariaDB.

Jalankan program dengan mengubah current directory ke src lalu membuka main.py: `python main.py`

## Modul
Berdasarkan use-case yang dikerjakan:
* Modul login
    ![login](./img/login.png)
* Modul register
    ![register](./img/register.png)
* Modul Keranjang Pembelian
    ![k](./img/keranjang.png)
* Modul Beli Produk
    ![a](./img/beranda.png)
    ![a](./img/detail_produk)
* Modul Pencarian Produk
    ![a](./img/search.png)
* Modul Review Produk
    ![-](./img/rating.jpg)
* Modul Form Pembayaran
    ![a](./img/form_bayar.png)
* Modul Transaksi
    ![-](./img/transaksi.png)

## Implementasi Basis Data
* Daftar tabel
![table](./img/table.png)
* Tabel user
![user](./img/user.png)
* Tabel toko
![toko](./img/toko.png)
* Tabel rating
![rating](./img/rating.png)
* Tabel pesanan
![pesanan](./img/pesanan.png)
* Tabel transaksi
![transaksi](./img/transaksi.png) 
* Tabel cart
![cart](./img/cart.png)
