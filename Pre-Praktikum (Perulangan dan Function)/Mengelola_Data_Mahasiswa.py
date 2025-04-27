# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan data mahasiswa ke dalam list
def create():
    # Variabel lokal 'nama' untuk menyimpan input nama mahasiswa sementara
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)  # Tambahkan nama ke list global
    print(f"'{nama}' berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data mahasiswa
def read():
    # Cek apakah list kosong
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
    else:
        print("Daftar Mahasiswa:")
        # Tampilkan semua nama mahasiswa beserta indeksnya
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}. {nama}")

# Fungsi untuk mengubah nama mahasiswa berdasarkan indeks
def update():
    read()  # Tampilkan data mahasiswa terlebih dahulu
    try:
        # Minta input indeks yang akan diubah
        index = int(input("Masukkan indeks yang ingin diubah: "))
        # Validasi apakah indeks berada dalam jangkauan list
        if 0 <= index < len(data_mahasiswa):
            # Variabel lokal 'nama_baru' untuk menyimpan nama yang baru
            nama_baru = input("Masukkan nama baru: ")
            data_mahasiswa[index] = nama_baru  # Ubah data pada indeks tersebut
            print("Data berhasil diubah.")
        else:
            print("Indeks tidak valid.")  # Jika indeks tidak sesuai
    except ValueError:
        print("Input tidak valid. Masukkan angka.")  # Jika input bukan angka

# Fungsi untuk menghapus nama mahasiswa berdasarkan indeks
def delete():
    read()  # Tampilkan data mahasiswa terlebih dahulu
    try:
        # Minta input indeks yang akan dihapus
        index = int(input("Masukkan indeks yang ingin dihapus: "))
        # Validasi apakah indeks berada dalam jangkauan list
        if 0 <= index < len(data_mahasiswa):
            # Hapus data menggunakan pop() dan simpan nama yang dihapus
            nama = data_mahasiswa.pop(index)
            print(f"'{nama}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")  # Jika indeks tidak sesuai
    except ValueError:
        print("Input tidak valid. Masukkan angka.")  # Jika input bukan angka

# Fungsi utama untuk menjalankan menu dan program utama
def main():
    while True:  # Loop utama agar program terus berjalan sampai user memilih keluar
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")  # Input menu dari user
        
        if pilihan == '1':
            create()  # Panggil fungsi create
        elif pilihan == '2':
            read()  # Panggil fungsi read
        elif pilihan == '3':
            update()  # Panggil fungsi update
        elif pilihan == '4':
            delete()  # Panggil fungsi delete
        elif pilihan == '5':
            print("Keluar dari program.")
            exit()  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Jika input menu salah

# Panggil fungsi main untuk memulai program
main()