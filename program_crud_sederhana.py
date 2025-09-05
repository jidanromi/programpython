# program_crud_sederhana.py
# Program CRUD Sederhana untuk Mengelola Data Buku

import json
import os

FILE_NAME = "data_buku.json"

def muat_data():
    """Memuat data dari file JSON jika ada"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def simpan_data(data):
    """Menyimpan data ke file JSON"""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def tampilkan_buku(daftar_buku):
    """Menampilkan semua buku"""
    print("\n=== DAFTAR BUKU ===")
    if not daftar_buku:
        print("Tidak ada data buku.")
        return
    
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. Judul: {buku['judul']}")
        print(f"   Penulis: {buku['penulis']}")
        print(f"   Tahun: {buku['tahun']}")
        print(f"   ISBN: {buku['isbn']}")
        print("-" * 30)

def tambah_buku(daftar_buku):
    """Menambah buku baru"""
    print("\n=== TAMBAH BUKU BARU ===")
    
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tahun = input("Tahun terbit: ")
    isbn = input("ISBN: ")
    
    buku_baru = {
        'judul': judul,
        'penulis': penulis,
        'tahun': tahun,
        'isbn': isbn
    }
    
    daftar_buku.append(buku_baru)
    simpan_data(daftar_buku)
    print("Buku berhasil ditambahkan!")

def edit_buku(daftar_buku):
    """Mengedit data buku"""
    tampilkan_buku(daftar_buku)
    
    if not daftar_buku:
        return
    
    try:
        index = int(input("\nPilih nomor buku yang akan diedit: ")) - 1
        if 0 <= index < len(daftar_buku):
            buku = daftar_buku[index]
            
            print(f"\nEdit buku: {buku['judul']}")
            buku['judul'] = input(f"Judul baru ({buku['judul']}): ") or buku['judul']
            buku['penulis'] = input(f"Penulis baru ({buku['penulis']}): ") or buku['penulis']
            buku['tahun'] = input(f"Tahun baru ({buku['tahun']}): ") or buku['tahun']
            buku['isbn'] = input(f"ISBN baru ({buku['isbn']}): ") or buku['isbn']
            
            simpan_data(daftar_buku)
            print("Buku berhasil diedit!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

def hapus_buku(daftar_buku):
    """Menghapus buku"""
    tampilkan_buku(daftar_buku)
    
    if not daftar_buku:
        return
    
    try:
        index = int(input("\nPilih nomor buku yang akan dihapus: ")) - 1
        if 0 <= index < len(daftar_buku):
            buku = daftar_buku.pop(index)
            simpan_data(daftar_buku)
            print(f"Buku '{buku['judul']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

def cari_buku(daftar_buku):
    """Mencari buku berdasarkan judul"""
    kata_kunci = input("\nMasukkan judul buku yang dicari: ").lower()
    
    hasil_pencarian = [
        buku for buku in daftar_buku 
        if kata_kunci in buku['judul'].lower()
    ]
    
    if hasil_pencarian:
        print(f"\nDitemukan {len(hasil_pencarian)} buku:")
        tampilkan_buku(hasil_pencarian)
    else:
        print("Buku tidak ditemukan.")

def main():
    """Program utama"""
    daftar_buku = muat_data()
    
    while True:
        print("\n=== SISTEM MANAJEMEN BUKU ===")
        print("1. Tampilkan semua buku")
        print("2. Tambah buku")
        print("3. Edit buku")
        print("4. Hapus buku")
        print("5. Cari buku")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tampilkan_buku(daftar_buku)
        elif pilihan == '2':
            tambah_buku(daftar_buku)
        elif pilihan == '3':
            edit_buku(daftar_buku)
        elif pilihan == '4':
            hapus_buku(daftar_buku)
        elif pilihan == '5':
            cari_buku(daftar_buku)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()