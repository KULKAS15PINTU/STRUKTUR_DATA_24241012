# Membuat berbagai tuple
t = (1234, 'Hello World')
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # Tanpa tanda kurung juga valid
t3 = ()                   # Tuple kosong
t4 = (5,)                 # Tuple satu elemen, perlu koma!

# Membuat tuple singleton (1 elemen)
satu = ('Isi',)
dua = "ini adalah tuple?",

# Cek tipe data
print(type(satu))  # <class 'tuple'>
print(type(dua))   # <class 'tuple'>

# Jika tidak pakai koma, bukan tuple
satu = ('Isi')
dua = "ini adalah tuple?"

# Cek tipe data
print(type(satu))  # <class 'str'>
print(type(dua))   # <class 'str'>

# Membuat tuple dan mengakses elemen
nama = ('Adam', 'Bachtiar', 'Maulachela')
print(nama[1])  # Output: Bachtiar

# Tuple tidak bisa diubah
t = (1, 5, 10, 15)
# t[0] = 0  # Ini akan error karena tuple immutable

# Memotong tuple (slicing)
angka = (10, 20, 30, 40)
print(angka[1:3])  # Output: (20, 30)
print(angka[:2])   # Output: (10, 20)
print(angka[2:])   # Output: (30, 40)

# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)

# Sequence Unpacking
# mula-mula kita buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)

matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)
    print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)
total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")