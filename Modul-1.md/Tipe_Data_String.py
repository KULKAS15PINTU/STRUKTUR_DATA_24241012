a = 'Halo'
b = "Python"
c = """Ini adalah string multi baris"""
print(type(a)) # <class 'str'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'str'>

# indexing dan slicing
text = "python"
print(text[0])    # Output: P
print(text[-1])   # Output: n
print(text[0:3])  # Output: Pyt
print(text[:4])   # Outpu: Pyth
print(text[::2])  # Otput: Pto (loncatan 2 karakter)

# operasi penggabungan string
print('Hello ' + 'World')

# operasi pengulangan string
print('Hi' * 3)

# operasi pengecekan string
print('a' in 'data')

# operasi panjang string
print(len('python'))

# fungsi dan string
s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.capitalize())  # 'Python programming'
print(s.title())       # 'Python Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['python', 'programming']
print(s.find("gram"))  # 10

# String format menggunakan F-String
name = "Adam"
age = 25
print(f"Halo, nama saya {name}, umur saya {age}")

# String format menggunakan F-String
name = "Adam"
age = 25
print(f"Halo, nama saya {name}, umur saya {age}")

# membuat list
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True]
kosong = []

# memanggil list
print(angka)
print(buah)
print(campuran)
print(kosong)

# indexing dan slicing pada list
data = ["a", "b", "c", "d"]
print(data[0])      # Output: a
print(data[-1])     # Output: d
print(data[1:3])    # Output: ['b', 'c']
print(data[:2])     # Output: ['a', 'b']

# Operasi penambahan anggota list
data = [1, 2, 3, 4, 5]
data = data + [10, 20]
print(data)

# Operasi pengulangan list
list = [1, 2]
list = list * 3
print(list)

# Operasi mengukur panjang list
print(len(data))
print(len(list))

# Operasi mengecek keanggotaan pada list
print(20 in data)
print(13 in list)

# Fungsi pada list 
a = [3, 1, 4, 1, 5]
print(a)
a.append(9)         # Menambahkan elemen di akhir
print(a)
a.insert(2, 7)      # Menyisipkan angka 7 di indeks ke-2
print(a)
a.remove(1)         # Menghapus elemen pertama yang bernilai 1
print(a)
a.pop()             # Menghapus elemen terakhir
print(a)
a.sort()            # Mengurutkan list secara ascending
print(a)
a.reverse()         # Membalik urutan elemen
print(a)
print(a.index(4))   # Mengembalikan indeks dari nilai 4
print(a.count(1))   # Menghitung jumlah kemunculan angka 1

# membuat matriks dari list bersarang
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# memanggil matriks
print(matrix)
# memanggil elemen list pada indeks [1][2]
print(matrix[1][2])  # Output: 6