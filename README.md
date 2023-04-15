# KASIR SUPERMARKET PAK ANDI
sistem kasir sederhana yang dibutuhkan oleh pak andi selaku pemilik supermarket. sistem kasi ini memungkinkan pelanggan untuk menambahkan barang kedalam keranjang belanja, baik nama barang, jumlah barang, maupun harga barang. selain itu kasir ini juga memungkinkan pelanggan untuk mengupdate nama, jumlah, maupun harga barang sudah diinput. pelanggan juga bisa menghapus belanjaan yang salah input atau tidak diinginkan lagi atau juga bisa menghapus seluruh isi keranjang.
# Baground Project
pak andi memiliki supermarket besar disalah satu kota diindonesia . andi memiliki rencana untuk melakukan perbaikan proses bisnis dengan membuat sistem kasir self service disupermarketnya sehingga customer bisa memasukkan item yang dibeli , jumlah yang dibeli dan harga item yang dibeli dan juga fitur fitur lainnya.
# Objective 
1. Membuat ID transaksi customer
2. Memungkinkan untuk menginput nama item, jumlah dan harga barang
3. Customer bisa mengupdate nama item, jumlah item, dan harga item
4. Customer bisa menghapus item
5. Customer bisa mereset seluruh isi keranjang belanja
6. Bisa menampilkan seluruh list yang ada dikeranjang belanja
7. menghitung total harga dan total harga setelah diskon
# Flowchart
![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/Cuplikan%20layar%202023-04-13%20165739.png?raw=true)
# PROGRAM FUNCTION
system kasir ini memiliki 2 file yaitu main.py dan modul.py.
1. main.py berfungsi untuk menjalankan main menu pada kasir ini dan memungkinkan pelanggan untuk memilih pilihan di main menu
2. modul.py berisi class transaction untuk yang bisa dipakai didalam file menu

Main.py

from modul import Transaction as transaction

while True:
    print("\n------------ Supermarket Andi -------------")
    print("-------------- Main Menu ------------------\n")
    print("1. Tambah Item")
    print("2. Ubah Nama Item")
    print("3. ubah quantity")
    print("4. ubah harga")
    print("5. Hapus Item")
    print("6. Reset Keranjang Belanja")
    print("7. Lihat Keranjang Belanja")
    print("8. Lihat Total Harga")
    print("9. Keluar")

    choice = input("Masukkan pilihan (1-9): ")
    print("\n")

    if choice == "1":
        transaction.add_item()
    elif choice == "2":
        transaction.update_name_item()
    elif choice == "3":
        transaction.update_quantity_item()
    elif choice == "4":
        transaction.update_price_item()
    elif choice == "5":
        transaction.delete_item()
    elif choice == "6":
        transaction.reset_order()
    elif choice == "7":
        transaction.check_list_order()
    elif choice == "8":
        transaction.total_price()
    elif choice == "9":
        print("Terima kasih telah berbelanja di Supermarket Andi")
        break
    else:
        print("Pilihan tidak benar. Masukkan pilihan (1-9)")
        
        
modul.py

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
 add item
 
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
update nama

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
update harga

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
update harga

    def update_price_item(self):#fungsi ini untuk mnegubah harga pada item didalam keranjang belanja
      print("------------ Update harga  ------------\n")
      nama_item = input("Masukkan nama Item yang akan diganti harganya: ")#untuk menginputkan nama lama yang akan diganti
      harga_baru = int(input("Harga baru dari item yang yang ingin diganti: "))#menginputkan harga baru 
      print ("\n")
      self.keranjang[nama_item][1] = harga_baru

      total_harga_baru = self.keranjang[nama_item][0] * harga_baru
      self.keranjang[nama_item][2] = total_harga_baru
      print(f'Item {nama_item} berhasil diubah harganya!\n')

 Menghapus item 
 
    def delete_item(self): #fungsi ini untuk mengahpus belanjaan yang tidak diinginkan
        print("---------------- Hapus Item ----------------\n")
        while True:     
            nama_item = input("Masukkan nama item yang ingin Anda hapus dari keranjang: ")
            if nama_item in self.keranjang:
                del self.keranjang[nama_item]#menghapus item yang dipilih
                print(f'Item {nama_item} berhasil dihapus dari keranjang!\n') #menampilkan laporan berhasil dihapus
                break
                
Mereset seluruh orderan

    def reset_order(self):#fungsi untuk meresetatau menghapus keseluruhan keranjang belanja
        print("------------ Reset Order  ------------\n")
        self.keranjang.clear()#hapus semuanya
        print("Anda berhasil menghapus seluruh item dalam keranjang!")

    def list_order(self):#untuk menampilkan semua barang yang dibeli
        print("------------ List Transaction  ------------\n")
        kolom = pd.DataFrame.from_dict(self.keranjang, orient='index', columns=['Jumlah', 'Harga', 'Total Harga'])
        print(kolom)

Menghitung total harga serta diskon 

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
# Test Case
Pada bagian ini kita melakukan test code yang sudah kita buat diatas.
1. customer menambahkan item kedalam keranjang belanja
![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/tambah%20item.png?raw=true)
2. customer mengupdate nama item

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/update%20nama.png?raw=true)

3. customer mengupdate jumlah

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/update%20jumlah.png?raw=true)

4. Customer mengupdate harga

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/update%20harga.png?raw=true)

5. customer menghapus item yang tidak diinginkan

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/hapus%20item.png?raw=true)

6. customer melakukan reset item

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/reset%20item.png?raw=true)

7. customer mengecek keranjang belanja

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/keranjang%20belanja.png?raw=true)

8. customer melihat keranjang belanja

![alt text](https://github.com/nime123/kasir-supermarket-pak-andi/blob/main/total%20belanja.png?raw=true)

#coclusion
berdasarkan requrements yang ada, semuanya biasa berjalan sesuai dengan harapan dan keinginan . dan memudahkan customer untuk menginput, mnegupdate, menghapus serta melakukan perhitungan total belanja.

#Future development
1. menambah grapict user interface agar lebih menarik dan lebih  mudah digunakan.
2. melakukan pencarian item yang pelanggan inginkan.
















