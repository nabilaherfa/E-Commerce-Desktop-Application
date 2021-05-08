# IF2250-2021-K04-04-Planties
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
    Penanggung Jawab : Karina Imani (NIM 13519166)
    -
    ![login](./img/login.png)
* Modul register
    Penanggung Jawab : Karina Imanni (NIM 13519166)
    -
    ![register](./img/register.png)
* Modul Keranjang Pembelian
    Penanggung Jawab : Akifa Nabil Ufairah (NIM 13519179)
    -
    ![k](./img/keranjang.png)
* Modul Beli Produk
    Penanggung Jawab : Akifa Nabil Ufairah (NIM 13519179)
    -
    ![a](./img/beranda.png)
    ![a](./img/detail_produk)
* Modul Pencarian Produk
    Penanggung Jawab : Clarissa Natalia (NIM 13519213)
    -
    ![a](./img/search.png)
* Modul Review Produk
    Penanggung Jawab : Nabilah Erfariani (NIM 13519181)
    -
    ![-](./img/rating.jpg)
* Modul Form Pembayaran
    Penanggung Jawab : Nabilah Erfariani (NIM 13519181)
    -
    ![a](./img/form_bayar.png)
* Modul Transaksi
    Penanggung Jawab : Nabilah Erfariani (NIM 13519181)
    -
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
