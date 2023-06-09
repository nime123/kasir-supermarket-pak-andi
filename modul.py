# -*- coding: utf-8 -*-
"""modul

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sv8wZ87KXGnNbgTW44RQy0DSrzTL8mGq
"""

import pandas as pd

class Transaction():
    def __init__(self):
        self.keranjang = {}
        self.total_belanja = 0

    def check_list_order(self): #fungsi ini untuk menampilkan isi keranjang yang sudah diinput
        print("----------- Keranjang Belanja  -----------\n")
        if not self.keranjang:
            print("Keranjang Anda masih kosong\n")
        else:
            kolom = pd.DataFrame.from_dict(self.keranjang, orient='index', 
            columns=['Jumlah', 'Harga', 'Total Harga'])
            print(kolom.to_string(header=True, index=True))
            print("\n")
    
    def add_item(self):#fungsi ini memungkinkan customer menginput belanjaan kedalam keranjang
        print("--------------- Tambah Item  --------------\n")
        while True:
            nama_item = input("Masukkan Nama Item: ") #input nama
            print ("\n")
            jumlah_item = int(input("Masukkan jumlah item: "))#input jumlah
            harga_item = int(input("Masukkan harga item: "))#input harga
            print ("\n")
            if nama_item in self.keranjang:
                print(f'{nama_item} Terdapat pada keranjang. Item akan diupdate.')
                print ("\n") 
                jumlah_baru = self.keranjang[nama_item][0] + jumlah_item
                harga_total = self.keranjang[nama_item][1] * jumlah_baru
                self.keranjang[nama_item][0] = jumlah_baru
                self.keranjang[nama_item][2] = harga_total
            else:  
                total_harga = jumlah_item * harga_item
                self.keranjang[nama_item] = [jumlah_item, harga_item, total_harga]
                print(f'Item {nama_item} dengan jumlah {jumlah_item} item berhasil ditambahkan\n')
            break

    def update_name_item(self):#fungsi ini untuk pelanggan mengubah nama barang yang sudah diinput sebelumnya dengan nama baru
        print("-------------- Ubah Nama Item  --------------\n")
        if not self.keranjang:
            print("Keranjang Anda masih kosong\n")
            return
        while True: 
            nama_item = input("Masukkan nama Item yang ingin Anda ubah: ")
            if nama_item in self.keranjang:
                print(f"\nItem {nama_item} ada dalam keranjang!\n") 
                break
            else:
                print(f"\nItem {nama_item} tidak ada dalam keranjang. \nMasukkan nama Item dengan benar.\n") 
        nama_item_baru = input("Masukkan nama baru: ")
        print ("\n")
        self.keranjang[nama_item_baru] = self.keranjang[nama_item]
        del self.keranjang[nama_item]
        print(f'Nama Item {nama_item} berhasil diubah menjadi {nama_item_baru}\n')
        self.check_list_order()

    def update_quantity_item(self):#fungsi untuk mengubah jumlah yang sudah diinput
        print("------------ Update Quantity  ------------\n")
        nama_item = input("Masukkan nama Item yang ingin Anda ubah: ")
        jumlah_baru = int(input("Jumlah item yang yang ingin diubah: "))
        print ("\n")

        self.keranjang[nama_item][0] = jumlah_baru
        #Mengundang nama item pada keranjang belanja untuk diganti menjadi nama item baru
        total_harga_baru = self.keranjang[nama_item][1] * jumlah_baru
        self.keranjang[nama_item][2] = total_harga_baru
        print(f'Jumlah dari Item {nama_item} berhasil diubah menjadi {jumlah_baru}')

    def update_price_item(self):#fungsi ini untuk mnegubah harga pada item didalam keranjang belanja
      print("------------ Update harga  ------------\n")
      nama_item = input("Masukkan nama Item yang akan diganti harganya: ")#untuk menginputkan nama lama yang akan diganti
      harga_baru = int(input("Harga baru dari item yang yang ingin diganti: "))#menginputkan harga baru 
      print ("\n")
      self.keranjang[nama_item][1] = harga_baru

      total_harga_baru = self.keranjang[nama_item][0] * harga_baru
      self.keranjang[nama_item][2] = total_harga_baru
      print(f'Item {nama_item} berhasil diubah harganya!\n')

      
    def delete_item(self): #fungsi ini untuk mengahpus belanjaan yang tidak diinginkan
        print("---------------- Hapus Item ----------------\n")
        while True:     
            nama_item = input("Masukkan nama item yang ingin Anda hapus dari keranjang: ")
            if nama_item in self.keranjang:
                del self.keranjang[nama_item]#menghapus item yang dipilih
                print(f'Item {nama_item} berhasil dihapus dari keranjang!\n') #menampilkan laporan berhasil dihapus
                break
           
    def reset_order(self):#fungsi untuk meresetatau menghapus keseluruhan keranjang belanja
        print("------------ Reset Order  ------------\n")
        self.keranjang.clear()#hapus semuanya
        print("Anda berhasil menghapus seluruh item dalam keranjang!")

    def list_order(self):#untuk menampilkan semua barang yang dibeli
        print("------------ List Transaction  ------------\n")
        kolom = pd.DataFrame.from_dict(self.keranjang, orient='index', columns=['Jumlah', 'Harga', 'Total Harga'])
        print(kolom)

    def total_price(self): #fungsi untuk menampilkan total harga, potongan diskon, dan total yang harus dibayar
       print("------------ Total Price  ------------\n")
       for item in self.keranjang:  
        self.total_belanja += self.keranjang[item][2]
        #kondisi dan totalan besaran diskon yang didapat berdasarkan besarnya total belanjaan
        if self.total_belanja > 200000:
            diskon = 0.05
        elif self.total_belanja > 300000:
            diskon = 0.08
        elif self.total_belanja > 500000:
            diskon = 0.1
        else:
            diskon = 0

        total_diskon = diskon * self.total_belanja
        total_harga_diskon = self.total_belanja - total_diskon#menghitung total harga setelah kena diskon

        print(f'Total belanja Anda setelah diskon Rp {total_harga_diskon}')


transaction = Transaction()